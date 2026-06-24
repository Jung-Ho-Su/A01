import pandas as pd

# 1. 원본 데이터 불러오기
file_path = "서울교통공사_역별 시간대별 승하차인원(23.1~23.12).csv"

# 공공데이터 인코딩 예외 처리 (cp949 또는 utf-8)
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='utf-8')

print(f"✅ 원본 데이터 로딩 완료 (총 {len(df):,}행)")

# 2. '승하차구분' 컬럼에서 '하차'에 해당하는 행만 필터링
# 💡 만약 24년도 데이터라면 컬럼명이 '구분'일 수 있으니 확인 후 수정이 필요할 수 있습니다.
target_col = '승하차구분' if '승하차구분' in df.columns else '구분'
df_alighting_only = df[df[target_col] == '하차']

# 3. 새로운 CSV 파일로 저장
# utf-8-sig를 사용하여 엑셀에서도 한글이 깨지지 않도록 합니다.
output_filename = "서울교통공사_23년도_하차인원만_추출.csv"
df_alighting_only.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 하차 데이터 추출 완료! (추출된 행: {len(df_alighting_only):,}개)")
print(f"✅ 생성된 파일명: {output_filename}")