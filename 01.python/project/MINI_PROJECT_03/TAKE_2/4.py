import pandas as pd

# 1. 24년도 원본 데이터 불러오기
file_path = "서울교통공사_역별 시간대별 승하차인원(24.1~24.12).csv"

# 24년도 공공데이터는 utf-8 인코딩이 기본인 경우가 많습니다.
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

print("✅ 데이터 로딩 완료! 24년도 승하차 인원 합산을 시작합니다...")

# 2. 날짜 컬럼 이름 확인 및 지정 (24년도는 '날짜'로 되어 있음)
date_col = '날짜' if '날짜' in df.columns else '수송일자'

# 데이터를 하나로 묶을 공통 기준열(Key) 설정
keys = [date_col, '호선', '역번호', '역명']

# 3. 시간대 컬럼만 추출 ('구분'과 같은 텍스트 컬럼 제외)
time_cols = [col for col in df.columns if '시' in col and col not in ['구분', '승하차구분']]

# 4. 공통 기준열을 바탕으로 그룹화(groupby)한 뒤, 시간대별 숫자를 모두 더하기(sum)
df_sum = df.groupby(keys)[time_cols].sum().reset_index()

# 5. 향후 23년도 데이터와 병합하기 쉽도록 컬럼명 통일 ('날짜' -> '수송일자')
if date_col == '날짜':
    df_sum.rename(columns={'날짜': '수송일자'}, inplace=True)

# 6. 새로운 CSV 파일로 저장
output_file = "서울교통공사_24년도_총이용객수(승차+하차).csv"
df_sum.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 원본 행 수: {len(df)}개")
print(f"✅ 승하차 합계 후 행 수: {len(df_sum)}개 (하나의 행으로 병합됨)")
print(f"✅ 새로 생성된 파일명: {output_file}")