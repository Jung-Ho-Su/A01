import pandas as pd

# 1. 24년도 원본 데이터 불러오기
file_path = "서울교통공사_역별 시간대별 승하차인원(24.1~24.12).csv"

# 인코딩 처리 (24년도 파일은 보통 utf-8로 인코딩되어 있습니다)
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

print(f"✅ 원본 데이터 로딩 완료 (총 {len(df):,}행)")

# 2. '구분' 컬럼에서 '하차'에 해당하는 행만 필터링
# 24년도 데이터의 경우 승하차 구분 컬럼명이 '구분'입니다.
df_alighting_only = df[df['구분'] == '하차']

# 3. 새로운 CSV 파일로 저장
# 엑셀에서도 한글이 깨지지 않도록 'utf-8-sig' 인코딩을 권장합니다.
output_filename = "서울교통공사_24년도_하차인원만_추출.csv"
df_alighting_only.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 하차 데이터 추출 완료! (추출된 행: {len(df_alighting_only):,}개)")
print(f"✅ 생성된 파일명: {output_filename}")