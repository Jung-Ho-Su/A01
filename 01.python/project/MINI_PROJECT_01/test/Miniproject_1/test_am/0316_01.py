import pandas as pd
import os


def filter_ulsan_arrivals():
    file_name = 'TCS_화물차전용(2_3_4_5종)_교통량.csv'

    if not os.path.exists(file_name):
        print(f"❌ '{file_name}' 파일이 없습니다. 경로를 확인해주세요.")
        return

    # 1. 파일 불러오기
    try:
        df = pd.read_csv(file_name, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_name, encoding='cp949')

    # 2. 정확한 검색을 위해 데이터 양옆의 공백 제거
    df['도착영업소명'] = df['도착영업소명'].astype(str).str.strip()

    # 3. 🎯 '울산' 도착 데이터만 완벽하게 필터링
    ulsan_df = df[df['도착영업소명'] == '울산'].copy()

    if ulsan_df.empty:
        print("❌ '울산'으로 도착한 데이터가 없습니다.")
        return

    # 4. 분석을 위한 보너스: '울산도착_화물차총합' 파생 변수 만들기
    # 도착지방향 2, 3, 4, 5종 차량 대수를 모두 더합니다.
    arrival_cols = ['도착지방향2종교통량', '도착지방향3종교통량', '도착지방향4종교통량', '도착지방향5종교통량']

    for col in arrival_cols:
        ulsan_df[col] = pd.to_numeric(ulsan_df[col], errors='coerce').fillna(0)

    ulsan_df['울산도착_화물차총합'] = ulsan_df[arrival_cols].sum(axis=1)

    # 5. 울산으로 화물차를 가장 많이 보낸 '출발지' 순으로 내림차순 정렬
    ulsan_df = ulsan_df.sort_values(by='울산도착_화물차총합', ascending=False)

    # 파이참 터미널 출력 설정 (표 잘림 방지)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # 6. 결과 출력 (상위 15개 출발지 확인)
    print("=" * 90)
    print("🏭 [울산 톨게이트 도착] 화물차(2~5종) 유입량 기준 상위 15개 출발지 목록")
    print("=" * 90)
    # 필요한 핵심 컬럼만 추려서 예쁘게 보여주기
    display_cols = ['집계일자', '출발영업소명', '도착영업소명', '울산도착_화물차총합'] + arrival_cols
    print(ulsan_df[display_cols].head(15).to_string(index=False))

    # 7. 추출된 데이터를 새로운 파일로 저장
    output_filename = '울산도착_화물차_교통량.csv'
    ulsan_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("\n" + "=" * 90)
    print(f"💾 총 {len(ulsan_df)}개의 '울산' 도착 노선이 '{output_filename}' 파일로 저장되었습니다!")
    print("=" * 90)


if __name__ == "__main__":
    filter_ulsan_arrivals()