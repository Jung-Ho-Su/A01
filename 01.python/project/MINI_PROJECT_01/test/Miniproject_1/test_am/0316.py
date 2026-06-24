import pandas as pd
import os


def extract_freight_traffic():
    # 1. 파일명 설정
    file_name = 'TCS_영업소간교통량_1일_1일_20260312.csv'

    if not os.path.exists(file_name):
        print(f"❌ '{file_name}' 파일이 없습니다. 경로를 확인해주세요.")
        return

    # 2. 한글 깨짐 방지 다중 인코딩 시도
    encodings = ['cp949', 'utf-8-sig', 'utf-8', 'euc-kr']
    df = None
    for enc in encodings:
        try:
            df = pd.read_csv(file_name, encoding=enc)
            print(f"✅ 파일 읽기 성공! (인코딩: {enc})\n")
            break
        except UnicodeDecodeError:
            continue

    if df is None:
        print("❌ 인코딩을 맞출 수 없어 파일을 열 수 없습니다.")
        return

    # 컬럼명의 공백 및 불필요한 따옴표 제거
    df.columns = df.columns.str.strip().str.replace('"', '')

    # 3. 🎯 남길 컬럼(열) 명시적으로 지정
    # 기본 정보 컬럼
    base_cols = ['집계일자', '출발영업소코드', '도착영업소코드', '출발영업소명', '도착영업소명']

    # 2, 3, 4, 5종 화물차 관련 컬럼 (도착지 방향 + 출발지 방향)
    freight_cols = [
        '도착지방향2종교통량', '도착지방향3종교통량', '도착지방향4종교통량', '도착지방향5종교통량',
        '출발지방향2종교통량', '출발지방향3종교통량', '출발지방향4종교통량', '출발지방향5종교통량'
    ]

    target_cols = base_cols + freight_cols

    # 해당 컬럼들만 추출해서 새로운 데이터프레임 생성
    filtered_df = df[target_cols].copy()

    # 파이참 터미널 출력 설정 (표 잘림 방지)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # 4. 결과 출력
    print("=" * 80)
    print("🚛 [화물차(2~5종) 데이터 추출 완료] 상위 10개 목록")
    print("=" * 80)
    print(filtered_df.head(10).to_string(index=False))

    # 5. 추출된 데이터를 새로운 파일로 저장
    output_filename = 'TCS_화물차전용(2_3_4_5종)_교통량.csv'
    filtered_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("\n" + "=" * 80)
    print(f"💾 총 {len(filtered_df):,}건의 정제된 데이터가 '{output_filename}' 파일로 저장되었습니다!")
    print("=" * 80)


if __name__ == "__main__":
    extract_freight_traffic()