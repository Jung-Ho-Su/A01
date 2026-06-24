import pandas as pd
import os


def extract_yearly_original_data():
    input_file = '산업별_종사자_현황_번역완료.csv'

    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' 파일을 찾을 수 없습니다.")
        return

    # 1. 데이터 불러오기 (헤더 없이 읽어서 직접 처리)
    df = pd.read_csv(input_file, encoding='utf-8-sig', header=None)

    # 헤더 위치 정의 (번역된 파일 기준)
    row_year = 0  # 2022.08, 2023.08 등
    row_type = 1  # 임금근로자, 상용근로자 등
    row_cat = 2  # 원지수, 증감 등

    # 2. 🎯 필요한 컬럼 인덱스 찾기
    # 첫 번째 컬럼('산업별')은 무조건 포함
    target_indices = [0]

    for i in range(1, len(df.columns)):
        year_val = str(df.iloc[row_year, i])
        type_val = str(df.iloc[row_type, i])
        cat_val = str(df.iloc[row_cat, i])

        # '임금근로자'의 '원지수'이면서 연도가 2022, 2023, 2024인 컬럼만 선택
        if type_val == '임금근로자' and cat_val == '원지수':
            if any(year in year_val for year in ['2022', '2023', '2024']):
                target_indices.append(i)

    # 3. 데이터 필터링 및 컬럼명 정리
    filtered_df = df.iloc[:, target_indices].copy()

    # 새로운 헤더 이름 설정
    new_headers = ['산업별']
    for idx in target_indices[1:]:
        year_label = str(df.iloc[row_year, idx]).split('.')[0]
        new_headers.append(f"{year_label}년 원지수")

    filtered_df.columns = new_headers

    # 헤더로 썼던 상위 3행은 제거하고 순수 데이터만 남김
    result_df = filtered_df.iloc[3:].reset_index(drop=True)

    # 4. 결과 저장
    output_filename = '산업별_연도별_원지수_추출.csv'
    result_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 60)
    print(f"✅ 연도별(2022-2024) 원지수 추출이 완료되었습니다.")
    print(f"💾 저장된 파일명: {output_filename}")
    print("=" * 60)
    print(result_df.head())


if __name__ == "__main__":
    extract_yearly_original_data()