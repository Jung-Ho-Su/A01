import urllib.request  # URL을 통해 데이터를 요청하고 응답을 받기 위한 파이썬 표준 라이브러리 임포트
import urllib.parse  # URL 인코딩(한글 변환)을 위해 필요한 라이브러리 추가
import datetime  # 현재 날짜와 시간 정보를 가져와 로그 출력 시 사용하기 위한 라이브러리 임포트
import json  # 네이버 API의 JSON 응답을 파이썬 객체로 다루기 위한 라이브러리 임포트
import csv  # 수집한 데이터를 CSV 형식으로 저장하기 위한 라이브러리 임포트
from config import *  # API 인증 정보(ID, Secret)가 들어있는 외부 파일(config.py)의 모든 변수를 가져옴


def get_request_url(url):  # 전달받은 URL로 네트워크 요청을 보내고 응답을 받아오는 함수 정의
    req = urllib.request.Request(url)  # 인자로 받은 URL 주소를 호출하기 위한 객체 생성
    req.add_header("X-Naver-Client-Id", client_id)  # 네이버 API 인증을 위해 헤더에 발급받은 클라이언트 아이디 추가
    req.add_header("X-Naver-Client-Secret", client_secret)  # 네이버 API 인증을 위해 헤더에 발급받은 클라이언트 시크릿 추가
    try:  # 예외 처리를 위해 실행을 시도하는 구문
        response = urllib.request.urlopen(req)  # 설정된 요청 정보로 서버에 접속하여 응답 객체를 받음
        if response.getcode() == 200:  # HTTP 상태 코드가 200(성공)인 경우 실행
            print("[%s] Url Request Success" % datetime.datetime.now())  # 현재 시간과 함께 요청 성공 메시지를 화면에 출력
            return response.read().decode('utf-8')  # 서버가 보낸 데이터를 읽어와서 UTF-8 형식으로 변환하여 반환
    except Exception as e:  # 요청 중 에러가 발생했을 때 처리하는 구문
        print(e)  # 발생한 에러 내용을 화면에 출력
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))  # 에러 발생 시간과 해당 URL을 출력하여 확인
        return None  # 에러 시 None 반환


def getNaverSearchResult(sNode, search_text, page_start, display):  # 검색 조건에 맞는 URL을 생성하고 결과를 받아오는 함수 정의
    base = "https://openapi.naver.com/v1/search"  # 네이버 검색 API의 기본 서비스 주소 설정
    node = "/%s.json" % sNode  # 검색할 분야(news 등)를 JSON 형식 주소로 설정
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text),
                                                    # 검색어(인코딩 포함), 시작 위치, 출력 개수를 파라미터로 조합
                                                    page_start, display)

    url = base + node + parameters  # 최종 요청 URL 완성
    retData = get_request_url(url)  # 데이터 요청

    if (retData == None):  # 받은 데이터가 없을 경우 처리
        return None
    else:
        return json.loads(retData)  # 문자열 형태의 JSON 데이터를 파이썬 객체로 변환하여 반환


def getPostData(post, jsonResult):  # 검색 결과 중 개별 뉴스 데이터에서 필요한 정보만 추출하는 함수 정의
    # 뉴스 노드(news)의 경우 title, originallink, link, description, pubDate 항목을 제공함
    title = post['title']  # 뉴스의 제목 정보를 추출
    description = post['description']  # 뉴스의 요약 내용 정보를 추출
    link = post['link']  # 해당 뉴스의 네이버 링크 정보를 추출
    pubDate = post['pubDate']  # 뉴스의 보도 시간 정보를 추출

    jsonResult.append({'title': title,  # 추출한 정보들을 딕셔너리 형태로 결과 리스트에 추가
                       'description': description,
                       'link': link,
                       'pubDate': pubDate})
    return


def main():  # 프로그램의 주 실행 흐름을 담당하는 메인 함수 정의
    jsonResult = []  # 최종 수집 결과를 저장할 빈 리스트 생성
    sNode = "news"  # 처리조건: news 정보 검색

    #### 처리조건 1: 검색 키워드를 아래 형식처럼 입력받도록 한다.
    search_text = input("검색키워드 입력 => ")
    display_count = 100  # 한 번의 요청으로 가져올 검색 결과 개수 설정

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)  # 첫 번째 검색 시도

    # 데이터 수집 (최대 1000개까지 반복)
    while ((jsonSearch != None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']:  # 응답 받은 뉴스 아이템을 하나씩 순회
            getPostData(post, jsonResult)  # 데이터 가공 및 추가

        nStart = jsonSearch['start'] + jsonSearch['display']  # 다음 시작 위치 계산
        if nStart > 100: break  # 네이버 API는 최대 100개까지만 지원하므로 탈출
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)  # 다음 페이지 요청

    # 처리조건 2: json형식으로 요청한 결과를 csv형식으로 저장한다.
    # 저장할 파일명: 검색키워드_naver.csv
    filename = '%s_naver.csv' % search_text

    if jsonResult:  # 수집된 데이터가 있을 경우에만 저장 실행
        with open(filename, 'w', encoding='utf-8-sig', newline='') as outfile:
            # CSV의 컬럼 헤더(키값) 설정
            fields = ['title', 'description', 'link', 'pubDate']
            writer = csv.DictWriter(outfile, fieldnames=fields)

            writer.writeheader()  # 첫 줄에 헤더 쓰기
            writer.writerows(jsonResult)  # 데이터 행들 쓰기

        print("%s SAVED" % filename)  # 저장 완료 메시지 출력
    else:
        print("검색 결과가 없어 파일을 저장하지 않았습니다.")


if __name__ == "__main__":  # 스크립트 직접 실행 시
    main()  # main 함수 실행