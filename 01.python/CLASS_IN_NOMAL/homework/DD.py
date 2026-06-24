from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


def get_blog_data(keyword):
    driver = webdriver.Chrome()  # 브라우저 실행
    driver.get('https://www.naver.com')  # 네이버 이동
    time.sleep(2)

    # 검색어 입력 및 엔터
    search_box = driver.find_element(By.ID, "query")
    search_box.send_keys(keyword + Keys.RETURN)
    time.sleep(2)

    # 블로그 탭 클릭 (텍스트로 시도 후 실패 시 XPATH 사용)
    try:
        driver.find_element(By.LINK_TEXT, "블로그").click()
    except:
        driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[5]/a').click()
    time.sleep(3)

    # 데이터 추출 (제목과 링크를 리스트 컴프리헨션 형식으로 수집)
    result = []
    items = driver.find_elements(By.CLASS_NAME, "sds-comps-text-type-headline1")

    for item in items:
        title = item.text
        link = item.find_element(By.XPATH, './ancestor::a').get_attribute('href')
        if title and link:
            result.append([title, link])

    driver.quit()  # 브라우저 종료
    return result


def main():
    query = input("검색 키워드 입력 : ")  # 키워드 입력
    blog_data = get_blog_data(query)  # 데이터 수집

    if len(blog_data) >= 10:
        print(f"\n검색 키워드 입력 : {query}\n")

        # 상위 10개 출력
        for t, l in blog_data[:10]:
            print(f"제목: {t}\n링크: {l}\n" + "-" * 32)

        # CSV 저장 (인코딩 포함)
        df = pd.DataFrame(blog_data, columns=['제목', '링크'])
        df.to_csv(f"naver_{query}.csv", index=False, encoding='utf-8-sig')
        print(f"\nnaver_{query}.csv 파일 저장 완료")
    else:
        print("검색 결과가 10개 미만입니다.")


if __name__ == '__main__':
    main()