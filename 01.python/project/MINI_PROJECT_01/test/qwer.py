import pandas as pd

# 1. 데이터 불러오기 (한글 인코딩 대응)
file_name = '행정구역_시도__연령별_경제활동인구_20260317131813.csv'
try:
    df = pd.read_csv(file_name, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_name, encoding='euc-kr')

# 2. 필터링할 지역 리스트 설정 (데이터 내 전체 명칭 기준)
target_cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시']

# 3. '고용률 (%)'에 해당하는 컬럼 찾기
# 데이터의 0번 행에 '고용률 (%)'이라는 서브 타이틀이 명시되어 있습니다.
employment_rate_cols = [col for col in df.columns if df.iloc[0][col] == '고용률 (%)']

# 4. 필요한 컬럼 선택 (식별을 위한 시도별, 연령계층별 포함)
cols_to_keep = ['시도별', '연령계층별'] + employment_rate_cols

# 5. 데이터 가공
# - 상단 타이틀 행(0번) 제외
# - 지정한 도시만 필터링
# - 필요한 컬럼만 추출
df_clean = df.drop([0])
df_filtered = df_clean[df_clean['시도별'].isin(target_cities)].copy()
df_final = df_filtered[cols_to_keep]

# 6. 결과 저장 (엑셀에서 바로 열 수 있도록 utf-8-sig 인코딩 사용)
output_file = 'filtered_employment_rate.csv'
df_final.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"가공 완료! '{output_file}' 파일이 생성되었습니다.")
print(df_final.head())