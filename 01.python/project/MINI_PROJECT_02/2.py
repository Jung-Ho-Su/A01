import pandas as pd

# 1. 파일 불러오기
file_path = '시군구.xlsx - Sheet1.csv'
df = pd.read_csv(file_path)

# 2. 시군구 정보를 통합 (시 컬럼 '1'과 군 컬럼 'Unnamed: 4' 중 값이 있는 것 선택)
# 시군구 구분을 위해 도(Unnamed: 2)와 시군구명을 합쳐서 그룹화합니다.
df['시군구_통합'] = df['1'].fillna(df['Unnamed: 4'])

# 3. 시군구별 데이터 개수(빈도) 계산
# 같은 도 내의 같은 시군구인 경우를 그룹화하여 개수를 셉니다.
counts = df.groupby(['Unnamed: 2', '시군구_통합']).size().reset_index(name='개수')

# 4. 계산된 개수를 원본 데이터에 병합 (옆 컬럼에 표시되도록 함)
df_result = df.merge(counts, on=['Unnamed: 2', '시군구_통합'], how='left')

# 5. 불필요한 임시 컬럼 제거 (선택 사항)
# df_result = df_result.drop(columns=['시군구_통합'])

# 6. 결과를 새로운 CSV 파일로 저장
output_file = '시군구_개수_결과.csv'
df_result.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"작업 완료! 결과가 '{output_file}' 파일로 저장되었습니다.")