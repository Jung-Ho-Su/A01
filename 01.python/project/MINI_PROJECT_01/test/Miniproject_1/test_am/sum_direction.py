import pandas as pd
import os


def calculate_row_totals():
    input_file = '전북출발_충남도착_교통량.csv'

    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' 파일을 찾을 수 없습니다.")
        return

    # 1. 데이터 불러오기
    try:
        df = pd.read_csv(input_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(input_file, encoding='cp949')

    # 2. 전처리: 컬럼명 따옴표 제거 및 불필요한 공백 제거
    df.columns = [col.strip().replace('"', '') for col in df.columns]

    # 3. 합산할 종별(1~6종) 컬럼 리스트 정의
    arrival_cols = [
        '도착지방향1종교통량', '도착지방향2종교통량', '도착지방향3종교통량',
        '도착지방향4종교통량', '도착지방향5종교통량', '도착지방향6종교통량'
    ]
    departure_cols = [
        '출발지방향1종교통량', '출발지방향2종교통량', '출발지방향3종교통량',
        '출발지방향4종교통량', '출발지방향5종교통량', '출발지방향6종교통량'
    ]

    # 4. 데이터 숫자형 변환 (계산을 위해 문자를 숫자로 강제 변환, 빈칸은 0)
    for col in arrival_cols + departure_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 5. 🎯 각 행별 합계 계산 (실제 수식 적용)
    # [도착지방향 합계 계산]
    df['도착지방향_교통량합계'] = df[arrival_cols].sum(axis=1)

    # [출발지방향 합계 계산]
    df['출발지방향_교통량합계'] = df[departure_cols].sum(axis=1)

    # [양방향 전체 총합 계산]
    df['전체_교통량_총합'] = df['도착지방향_교통량합계'] + df['출발지방향_교통량합계']

    # 6. 결과 저장
    output_filename = '전북출발_충남도착_교통량_계산완료.csv'
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 70)
    print(f"✅ 각 행별 데이터 합산 완료! (1종~6종 합산됨)")
    print(f"💾 최종 파일 저장됨: {output_filename}")
    print("=" * 70)

    # 확인용 미리보기 (상위 5개 행)
    preview_cols = ['출발영업소명', '도착영업소명', '도착지방향_교통량합계', '출발지방향_교통량합계', '전체_교통량_총합']
    print(df[preview_cols].head())


if __name__ == "__main__":
    calculate_row_totals()