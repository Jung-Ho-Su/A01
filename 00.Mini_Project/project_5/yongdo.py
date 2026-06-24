import pandas as pd

# 1. 파일 설정
file_path = '부산 영도구 공시지가.xlsx'

# 2. 데이터 불러오기 (엑셀 최적화)
try:
    # 엔진을 'openpyxl'로 명시하면 더 안정적입니다.
    # 만약 시트가 여러 개라면 sheet_name=0(첫 번째 시트)을 지정합니다.
    df = pd.read_excel(file_path, engine='openpyxl')
    print("엑셀 파일을 성공적으로 불러왔습니다.")
except Exception as e:
    print(f"엑셀 로드 실패, CSV로 재시도합니다: {e}")
    # 엑셀 읽기 실패 시 CSV(cp949)로 백업 시도
    df = pd.read_csv(file_path, encoding='cp949')

# 3. '영도구' 데이터 필터링 및 복사
# '부산광역시 영도구'가 포함된 행만 추출
df_yeongdo = df[df['법정동명'].str.contains('영도구', na=False)].copy()

# 4. '산'지 제외 (특수지구분명 기준)
df_filtered = df_yeongdo[df_yeongdo['특수지구분명'] != '산'].copy()

# 5. 지번 데이터 정제 (날짜 형식 및 비정상 지번 제거)
# 엑셀의 자동 변환 기능 때문에 '1-10'이 '01월 10일'이 된 데이터들을 걸러냅니다.
# 또한 지번이 문자열인지 확인하여 안전하게 처리합니다.
df_filtered['지번'] = df_filtered['지번'].astype(str)
df_filtered = df_filtered[~df_filtered['지번'].str.contains('월|일|Jan|Feb|Mar|Apr|May|Jun', na=False)]

# 6. 공시지가 수치화 및 결측치 제거
df_filtered['공시지가'] = pd.to_numeric(df_filtered['공시지가'], errors='coerce')
df_filtered = df_filtered.dropna(subset=['공시지가'])

# 7. 동별 최저가 추출 (중복 제거)
# 가격순 정렬 -> 법정동명 중복 제거(첫 번째 값=최저가 유지)
df_sorted = df_filtered.sort_values(by='공시지가', ascending=True)
df_unique_dong = df_sorted.drop_duplicates(subset=['법정동명'], keep='first')

# 8. 최종 Top 10 선정 및 저장
top_10_yeongdo = df_unique_dong.head(10)
output_file = 'yeongdo_final_top10.csv'

# 한글 깨짐 방지를 위해 utf-8-sig 사용
top_10_yeongdo.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n[성공] '{output_file}' 파일이 생성되었습니다.")
print("-" * 70)
print(top_10_yeongdo[['법정동명', '지번', '공시지가']].reset_index(drop=True))