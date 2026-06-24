import pandas as pd
import re
import os
from functools import reduce


def analyze_complex_trends():
    # 1. 대상 파일 목록 (2020~2025년 시도별 데이터)
    files = {
        '2020': '20 (연간보정)산업단지현황조사_2020년1분기(게시용).xlsx - 시도별.csv',
        '2021': '21 (연간보정)산업단지현황조사_2021년1분기(게시용)_22.12수정.xlsx - 시도별.csv',
        '2022': '22 산업단지현황조사_2022년 1분기(게시용)_연간보정(240314).xlsx - 시도별.csv',
        '2023': '23 산업단지현황조사_2023년 1분기(게시용)_연간보정(241121).xlsx - 시도별.csv',
        '2024': '24 산업단지현황조사_2024년 1분기(게시용)_연간보정(241121).xlsx - 시도별.csv',
        '2025': '25 산업단지현황조사_2025년 1분기(게시용)_연간보정(240918).xlsx - 시도별.csv'
    }

    dfs = []

    for year, file in files.items():
        if not os.path.exists(file):
            print(f"⚠️ 파일을 찾을 수 없습니다: {file}")
            continue

        # 2. 파일별로 다른 헤더(컬럼명) 위치 동적 탐색
        encodings = ['utf-8-sig', 'utf-8', 'cp949', 'euc-kr']
        lines = []
        for enc in encodings:
            try:
                with open(file, 'r', encoding=enc) as f:
                    lines = f.readlines()
                break
            except UnicodeDecodeError:
                continue

        header_idx = 0
        for i, line in enumerate(lines):
            # '구분'과 '단지수'라는 글자가 포함된 행을 데이터 시작(헤더)으로 인식
            if '구분' in line and '단지수' in line:
                header_idx = i
                break

        # 3. 데이터 불러오기
        df = None
        for enc in encodings:
            try:
                df = pd.read_csv(file, encoding=enc, skiprows=header_idx)
                break
            except Exception:
                continue

        if df is None or '구분' not in df.columns or '단지수' not in df.columns:
            continue

        # 4. 필요한 컬럼 추출 및 정제
        df = df[['구분', '단지수']].copy()

        # 결측치 및 의미 없는 빈 행 제거
        df = df.dropna(subset=['구분'])
        df = df[~df['구분'].astype(str).str.contains('Unnamed')]

        # '구분'명 통일 (예: '서울국가', '서울 국가' -> '서울국가'로 띄어쓰기 완전 제거)
        df['구분'] = df['구분'].astype(str).str.replace(r'\s+', '', regex=True)

        # '단지수' 정제 ('1,312개', '총47개', '47.0' 등에서 콤마 제거 후 숫자만 추출)
        df['단지수_str'] = df['단지수'].astype(str).str.replace(',', '')
        extracted = df['단지수_str'].str.extract(r'(\d+\.?\d*)')[0]
        df['단지수'] = pd.to_numeric(extracted, errors='coerce')

        # 변환 안 된 데이터 버리고 연도별로 컬럼명 세팅
        df = df.dropna(subset=['단지수'])
        df = df.drop_duplicates(subset=['구분'])
        df = df.rename(columns={'단지수': f'{year}년'})
        df = df[['구분', f'{year}년']]

        dfs.append(df)

    if not dfs:
        print("데이터를 처리하지 못했습니다.")
        return

    # 5. 연도별 데이터를 '구분' 컬럼 기준으로 하나로 병합 (Outer Join)
    final_df = reduce(lambda left, right: pd.merge(left, right, on='구분', how='outer'), dfs)

    # 6. 증감수 및 증감률(%) 계산 (2020년 대비 2025년 기준)
    final_df['증감수(25-20)'] = final_df['2025년'] - final_df['2020년']
    final_df['증감률(%)'] = (final_df['증감수(25-20)'] / final_df['2020년']) * 100

    # 소수점 둘째 자리까지 반올림
    final_df['증감률(%)'] = final_df['증감률(%)'].round(2)

    # 7. 최종 결과 저장
    output_path = '시도별_단지수_증감추이(2020_2025).csv'
    final_df.to_csv(output_path, index=False, encoding='utf-8-sig')

    # 결과 미리보기 출력
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print("=" * 90)
    print("📊 시도별 단지수 증감추이 미리보기 (TOP 10)")
    print("=" * 90)

    print(final_df.head(10).to_string(index=False))
    print(f"\n✅ 완료! 결과 파일이 저장되었습니다: {output_path}")


if __name__ == '__main__':
    analyze_complex_trends()