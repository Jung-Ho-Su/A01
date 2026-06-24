import pandas as pd

# 1. 2024년도 CSV 파일 불러오기
file_path_2024 = 'KC_624_DMSTC_MIEC_STATN_BIZAEA_2024.csv'
df_2024 = pd.read_csv(file_path_2024)

# 2. 'CTPRVN_NM' 컬럼에서 '인천광역시' 행만 필터링
incheon_2024 = df_2024[df_2024['CTPRVN_NM'] == '인천광역시']

# 3. 결과 저장 (인코딩은 한글 깨짐 방지를 위해 utf-8-sig 사용)
output_name = 'incheon_filtered_2024.csv'
incheon_2024.to_csv(output_name, index=False, encoding='utf-8-sig')

print(f"2024년 데이터 필터링 완료! '{output_name}' 파일로 저장되었습니다.")
print(f"추출된 인천광역시 데이터 수: {len(incheon_2024)}행")