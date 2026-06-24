import pandas as pd
import os


def calculate_final_totals():
    input_file = '전북_출발_통합_교통량_최종.csv'

    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return

    # 1. 데이터 불러오기 (한글 인코딩 처리)
    try:
        df = pd.read_csv(input_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(input_file, encoding='cp949')

    # 2. 전처리: 컬럼명 양끝 공백 및 따옴표 제거
    df.columns = [col.strip().replace('"', '') for col in df.columns]

    # 3. 합산할 대상 컬럼 리스트 (1종 ~ 6종)
    arrival_cols = [
        '도착지방향1종교통량', '도착지방향2종교통량', '도착지방향3종교통량',
        '도착지방향4종교통량', '도착지방향5종교통량', '도착지방향6종교통량'
    ]
    departure_cols = [
        '출발지방향1종교통량', '출발지방향2종교통량', '출발지방향3종교통량',
        '출발지방향4종교통량', '출발지방향5종교통량', '출발지방향6종교통량'
    ]

    # 4. 데이터 숫자형 변환 (문자가 섞여있을 경우를 대비해 0으로 처리하며 변환)
    for col in arrival_cols + departure_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 5. 🎯 행별 합계 계산
    # [전북 출발 방향 합계]
    df['전북출발_방향_합계'] = df[arrival_cols].sum(axis=1)

    # [전북 도착 방향 합계]
    df['전북도착_방향_합계'] = df[departure_cols].sum(axis=1)

    # [양방향 전체 통합 총합계]
    df['행별_전체_교통량_총합'] = df['전북출발_방향_합계'] + df['전북도착_방향_합계']

    # 6. 결과 저장
    output_filename = '전북_출발_통합_교통량_합계계산완료.csv'
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 70)
    print(f"✅ 모든 행에 대한 숫자 합산이 완료되었습니다.")
    print(f"💾 최종 파일이 저장되었습니다: {output_filename}")
    print("=" * 70)

    # 상위 5개 결과 미리보기
    preview_cols = ['출발영업소명', '도착영업소명', '전북출발_방향_합계', '전북도착_방향_합계', '행별_전체_교통량_총합']
    print(df[preview_cols].head())


if __name__ == "__main__":
    calculate_final_totals()