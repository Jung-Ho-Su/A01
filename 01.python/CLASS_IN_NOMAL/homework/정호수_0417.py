from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


def get_blog_data(keyword):
    # 1. 브라우저 실행 및 네이버 이동
    driver = webdriver.Chrome()
    driver.get('https://www.naver.com')
    time.sleep(2)

    # 2. 키워드 검색
    search_box = driver.find_element(By.ID, "query")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # 3. 블로그 탭 클릭 (상단 메뉴의 '블로그' 링크 텍스트로 찾기)
    try:
        driver.find_element(By.LINK_TEXT, "블로그").click()
    except:
        # 탭이 바로 안 보일 경우를 대비해 XPATH 등으로 재시도
        driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[5]/a').click()
    time.sleep(3)

    # 4. 블로그 데이터 추출 (최신 클래스명 반영)
    result = []
    # 제목 요소들을 가져옵니다.
    title_elements = driver.find_elements(By.CLASS_NAME, "sds-comps-text-type-headline1")

    for item in title_elements:
        title = item.text
        # 제목 요소의 상위 a 태그에서 링크(href)를 가져옵니다.
        link = item.find_element(By.XPATH, './ancestor::a').get_attribute('href')

        if title and link:
            result.append([title, link])

    driver.quit()
    return result


def main():
    # 처리조건 1: 검색 키워드 입력
    query = input("검색 키워드 입력 : ")

    # 데이터 수집
    blog_data = get_blog_data(query)

    if len(blog_data) >= 10:
        # 화면 출력 (문제의 <출력형식> 준수)
        print(f"\n검색 키워드 입력 : {query}\n")

        for data in blog_data[:10]:  # 10개 이상 출력
            print(f"제목: {data[0]}")
            print(f"링크: {data[1]}")
            print("--------------------------------")

        # 처리조건 2: CSV 파일 저장 (naver_검색키워드.csv)
        df = pd.DataFrame(blog_data, columns=['제목', '링크'])
        filename = f"naver_{query}.csv"
        # 한글 깨짐 방지를 위해 utf-8-sig 사용
        df.to_csv(filename, index=False, encoding='utf-8-sig')

        print(f"\n{filename} 파일 저장 완료")
    else:
        print("검색 결과가 10개 미만입니다.")


if __name__ == '__main__':
    main()