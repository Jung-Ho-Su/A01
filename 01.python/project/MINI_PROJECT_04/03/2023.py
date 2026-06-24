import pandas as pd

# 1. CSV 파일 불러오기
# 파일 경로가 업로드된 경로와 일치하는지 확인하세요.
file_path = 'KC_624_DMSTC_MIEC_STATN_BIZAEA_2023.csv'
df = pd.read_csv(file_path)

# 2. 'CTPRVN_NM'(시도명) 컬럼이 '인천광역시'인 행만 필터링
incheon_df = df[df['CTPRVN_NM'] == '인천광역시']

# 3. 필터링된 데이터를 새로운 CSV 파일로 저장
# encoding='utf-8-sig'는 한글 깨짐 방지를 위해 설정합니다.
output_file = 'incheon_filtered_data.csv'
incheon_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"필터링 완료! '{output_file}' 파일이 생성되었습니다.")
print(f"인천광역시 데이터 개수: {len(incheon_df)}개")
