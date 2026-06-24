import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta


def get_valid_date():
    """사용자로부터 유효한 날짜를 입력받는 함수"""
    while True:
        search_day = input("조회할 날짜를 입력하세요 (예: 20260402): ").strip()


        if len(search_day) != 8 or not search_day.isdigit():
            print("잘못된 형식입니다. YYYYMMDD 형식의 8자리 숫자로 입력해주세요.\n")
            continue

        try:

            input_date = datetime.strptime(search_day, "%Y%m%d").date()
            start_date = datetime(2006, 9, 22).date()

            yesterday = datetime.now().date() - timedelta(days=1)

            if start_date <= input_date <= yesterday:
                return search_day
            else:
                print(f"입력 가능한 날짜 범위를 벗어났습니다.")
                print(f"(가능 범위: 20060922 ~ {yesterday.strftime('%Y%m%d')})\n")
        except ValueError:
            print("달력에 존재하지 않는 유효하지 않은 날짜입니다. 다시 입력해주세요.\n")


def crawl_bugs_chart(search_day):
    """벅스 차트 데이터를 크롤링하는 함수"""
    url = f"https://music.bugs.co.kr/chart/track/day/total?chartdate={search_day}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')


    track_list = soup.select('table.trackList > tbody > tr')

    results = []
    for track in track_list:

        rank_tag = track.select_one('div.ranking > strong')
        rank = rank_tag.get_text(strip=True) if rank_tag else ""


        title_tag = track.select_one('p.title > a')
        title = title_tag.get_text(strip=True) if title_tag else ""


        singer_tag = track.select_one('p.artist > a')
        singer = singer_tag.get_text(strip=True) if singer_tag else ""


        if rank and title and singer:
            results.append([search_day, rank, singer, title])

    return results


def save_to_csv(search_day, data):
    """크롤링한 데이터를 CSV 파일로 저장하는 함수"""
    filename = f"bugschart_{search_day}.csv"


    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(['search_day', 'rank', 'singer', 'title'])

        writer.writerows(data)

    print(f"\n성공적으로 크롤링을 완료했습니다.")
    print(f"결과가 [{filename}] 파일로 저장되었습니다.")


if __name__ == "__main__":

    target_date = get_valid_date()


    print(f"\n{target_date} 일자 벅스 차트 데이터를 수집 중입니다...")
    chart_data = crawl_bugs_chart(target_date)


    if chart_data:
        save_to_csv(target_date, chart_data)
    else:
        print("해당 날짜의 차트 데이터를 찾을 수 없거나 크롤링에 실패했습니다.")