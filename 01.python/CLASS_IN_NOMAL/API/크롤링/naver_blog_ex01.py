import urllib.request   # URL을 통해 데이터를 요청하고 응답을 받기 위한 파이썬 표준 라이브러리 임포트
import datetime         # 현재 날짜와 시간 정보를 가져와 로그 출력 시 사용하기 위한 라이브러리 임포트
import json             # 수집한 데이터를 JSON 형식으로 변환하거나 파일로 저장하기 위한 라이브러리 임포트
from config import * # API 인증 정보(ID, Secret)가 들어있는 외부 파일(config.py)의 모든 변수를 가져옴

def get_request_url(url):   # 전달받은 URL로 네트워크 요청을 보내고 응답을 받아오는 함수 정의
    req = urllib.request.Request(url)                           # 인자로 받은 URL 주소를 호출하기 위한 객체 생성
    req.add_header("X-Naver-Client-Id", client_id)              # 네이버 API 인증을 위해 헤더에 발급받은 클라이언트 아이디 추가
    req.add_header("X-Naver-Client-Secret", client_secret)      # 네이버 API 인증을 위해 헤더에 발급받은 클라이언트 시크릿 추가
    try:                                                        # 예외 처리를 위해 실행을 시도하는 구문
        response = urllib.request.urlopen(req)                  # 설정된 요청 정보로 서버에 접속하여 응답 객체를 받음
        if response.getcode() == 200:                           # HTTP 상태 코드가 200(성공)인 경우 실행
            print("[%s] Url Request Success" % datetime.datetime.now()) # 현재 시간과 함께 요청 성공 메시지를 화면에 출력
            return response.read().decode('utf-8')              # 서버가 보낸 데이터를 읽어와서 UTF-8 형식으로 변환하여 반환
    except Exception as e:                                      # 요청 중 에러(404, 500 등)가 발생했을 때 처리하는 구문
        print(e)                                                # 발생한 에러 내용을 화면에 출력
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url)) # 에러 발생 시간과 해당 URL을 출력하여 확인
        return None                                             # 에러가 발생했으므로 아무 데이터도 반환하지 않음(None 반환)


def getNaverSearchResult(sNode, search_text, page_start, display):  # 검색 조건에 맞는 URL을 생성하고 결과를 받아오는 함수 정의
    base = "https://openapi.naver.com/v1/search"                # 네이버 검색 API의 기본 서비스 주소 설정
    node = "/%s.json" % sNode                                   # 검색할 분야(blog, news 등)를 JSON 형식 주소로 설정
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), # 검색어(인코딩 포함), 시작 위치, 출력 개수를 파라미터로 조합
                                                    page_start, display)

    url = base + node + parameters                              # 기본 주소, 노드, 파라미터를 합쳐 최종 요청 URL 완성

    retData = get_request_url(url)                              # 생성된 URL을 get_request_url 함수에 전달하여 데이터 요청

    if (retData == None):                                       # 받은 데이터가 없을 경우 처리
        return None                                             # 아무 값도 반환하지 않음
    else:                                                       # 성공적으로 데이터를 받았을 경우 처리
        return json.loads(retData)                              # 문자열 형태의 JSON 데이터를 파이썬 객체(딕셔너리/리스트)로 변환하여 반환


def getPostData(post, jsonResult):                              # 검색 결과 중 개별 포스트 데이터에서 필요한 정보만 추출하는 함수 정의
    title = post['title']                                       # 포스트의 제목(title) 정보를 추출
    description = post['description']                           # 포스트의 요약 내용(description) 정보를 추출
    bloggerlink = post['bloggerlink']                           # 블로거의 개인 주소(bloggerlink) 정보를 추출
    link = post['link']                                         # 해당 포스트의 원문 링크(link) 정보를 추출
    postdate = post['postdate']                                 # 포스트가 작성된 날짜(postdate) 정보를 추출
    bloggername = post['bloggername']                           # 블로거의 이름(bloggername) 정보를 추출

    jsonResult.append({'title': title, 'description': description, # 추출한 정보들을 딕셔너리 형태로 묶어 결과 리스트에 추가
                       'bloggerlink': bloggerlink, 'link': link,
                       'postdate': postdate, 'bloggername': bloggername})
    return                                                      # 함수 종료


def main():                                                     # 프로그램의 주 실행 흐름을 담당하는 메인 함수 정의
    jsonResult = []                                             # 최종 수집 결과를 저장할 빈 리스트 생성
    sNode = "blog"                                              # 검색 대상 노드를 'blog'로 설정
    search_text = "엔트로픽"                                     # 검색할 키워드를 '엔트로픽'으로 설정
    display_count = 100                                         # 한 번의 요청으로 가져올 검색 결과 개수를 100개로 설정

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count) # 1번 데이터부터 시작하여 첫 번째 검색 시도
    while ((jsonSearch != None) and (jsonSearch['display'] != 0)): # 검색 결과가 정상적으로 있고, 결과 개수가 0이 아닐 동안 반복
        for post in jsonSearch['items']:                        # 응답 받은 데이터 중 실제 게시물들(items)을 하나씩 순회
            getPostData(post, jsonResult)                       # 순회 중인 게시물 데이터를 정리하여 jsonResult 리스트에 추가

        nStart = jsonSearch['start'] + jsonSearch['display']    # 현재 시작 위치에 가져온 개수를 더해 다음 시작 위치 계산
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count) # 다음 페이지 데이터를 요청하여 갱신

    with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile: # '검색어_naver_blog.json' 파일을 쓰기 모드로 생성
        retJson = json.dumps(jsonResult,                        # 수집된 전체 리스트 데이터를 JSON 문자열로 변환
                             indent=4,                          # 가독성을 위해 4칸 들여쓰기 적용
                             sort_keys=True,                    # 키(key) 이름을 기준으로 오름차순 정렬
                             ensure_ascii=False)                # 한글이 깨지지 않도록 유니코드 그대로 저장
        outfile.write(retJson)                                  # 변환된 JSON 문자열을 실제 파일에 기록

    print("%s_naver_%s.json SAVED" % (search_text, sNode))      # 파일 저장 완료 메시지를 화면에 출력


if __name__ == "__main__":                                      # 현재 스크립트가 직접 실행되는 경우에만 아래 실행
    main()                                                      # main 함수 호출하여 프로그램 시작