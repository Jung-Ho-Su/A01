import pandas as pd
import os


def load_traffic_data():
    # 1. 다운로드 받은 파일명 입력 (경로가 다르다면 절대경로/상대경로 수정)
    file_name = 'TCS_영업소간교통량_1일_1일_20260312.csv'

    if not os.path.exists(file_name):
        print(f"❌ '{file_name}' 파일을 찾을 수 없습니다. 같은 폴더에 있는지 확인해주세요!")
        return

    # 2. 한글 깨짐 방지를 위한 다중 인코딩 시도
    encodings = ['cp949', 'utf-8-sig', 'utf-8', 'euc-kr']
    df = None

    for enc in encodings:
        try:
            df = pd.read_csv(file_name, encoding=enc)
            print(f"✅ 파일 읽기 성공! (사용된 인코딩: {enc})\n")
            break
        except UnicodeDecodeError:
            continue

    if df is None:
        print("❌ 인코딩을 맞출 수 없어 파일을 열 수 없습니다.")
        return

    # 3. 파이참 콘솔창에서 열(Column)이 생략(...)되지 않고 모두 보이도록 설정
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # 컬럼명에 포함된 불필요한 띄어쓰기(공백)나 따옴표 제거 (데이터 전처리 기초)
    df.columns = df.columns.str.strip().str.replace('"', '')

    # 4. 데이터 요약 정보 확인 (총 몇 줄인지, 컬럼명은 뭔지)
    print("=" * 50)
    print("📊 [1] 데이터 기본 정보 (info)")
    print("=" * 50)
    df.info()

    # 5. 상위 5개 데이터 미리보기
    print("\n" + "=" * 50)
    print("👀 [2] 데이터 미리보기 (상위 5행)")
    print("=" * 50)
    print(df.head())

    # 6. 간단한 필터링 테스트: 특정 영업소 출발 데이터만 보기 (예: 서울)
    print("\n" + "=" * 50)
    print("🚛 [3] 응용: '서울' 영업소 출발 데이터 요약 (도착지별 총교통량)")
    print("=" * 50)

    # 텍스트 데이터의 공백 제거
    df['출발영업소명'] = df['출발영업소명'].astype(str).str.strip()
    df['도착영업소명'] = df['도착영업소명'].astype(str).str.strip()

    seoul_departures = df[df['출발영업소명'] == '서울']

    if not seoul_departures.empty:
        # 목적지별 총 교통량이 많은 순으로 정렬해서 보여주기
        target_cols = ['출발영업소명', '도착영업소명', '도착지방향총교통량']
        top_destinations = seoul_departures[target_cols].sort_values(by='도착지방향총교통량', ascending=False)
        print(top_destinations.head(10).to_string(index=False))
    else:
        print("'서울' 출발 데이터가 없습니다.")


# 코드 실행
if __name__ == "__main__":
    load_traffic_data()