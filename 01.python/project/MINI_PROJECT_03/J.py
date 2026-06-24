import pandas as pd

# 1. 원본 파일 불러오기
file_path = "서울교통공사_역별 시간대별 승하차인원(24.1~24.12).csv"

# 인코딩 처리 (한글이 포함된 파일이므로 utf-8-sig 사용 권장)
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

# 2. '구분' 컬럼에서 '승차' 데이터만 필터링
df_boarding = df[df['구분'] == '승차']

# 3. 새로운 CSV 파일로 저장 (한글 깨짐 방지를 위해 utf-8-sig 사용)
output_file = "서울교통공사_24년도_승차인원만_추출.csv"
df_boarding.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"추출 완료: {len(df_boarding)}개의 승차 데이터가 '{output_file}'로 저장되었습니다.")