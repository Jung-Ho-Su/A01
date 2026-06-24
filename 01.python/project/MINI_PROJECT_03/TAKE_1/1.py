import pandas as pd

# 1. 원본 데이터 불러오기
file_path = "서울교통공사_역별 시간대별 승하차인원(23.1~23.12).csv"

# 인코딩 처리 (공공데이터는 보통 cp949나 utf-8 사용)
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='utf-8')

print(f"✅ 원본 데이터 행 수: {len(df)}개")

# 2. '하차' 행을 지우고, '승하차구분' 컬럼이 '승차'인 행만 남기기
df_boarding_only = df[df['승하차구분'] == '승차']

# 3. 새로운 CSV 파일로 저장
# 엑셀에서 한글이 깨지는 것을 방지하기 위해 encoding='utf-8-sig'를 사용합니다.
output_filename = "서울교통공사_승차인원만_추출.csv"
df_boarding_only.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 필터링 완료! 저장된 행 수: {len(df_boarding_only)}개")
print(f"✅ 새로 생성된 파일명: {output_filename}")