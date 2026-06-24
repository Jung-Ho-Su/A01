import pandas as pd

# 1. 파일 불러오기 (앞서 추출한 승차인원 파일)
file_path = "서울교통공사_승차인원만_추출.csv"

# 인코딩 처리 (한글 깨짐 방지)
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='cp949')
    except:
        df = pd.read_csv(file_path, encoding='utf-8')

print(f"✅ 원본 데이터 행 수: {len(df)}개")

# 2. '수송일자' 컬럼을 기준으로 2023년도와 2024년도 데이터만 필터링
# 날짜 데이터를 문자열(String)로 변환한 뒤, 앞 4자리가 '2023' 이거나 '2024'인 행만 남깁니다.
df['수송일자'] = df['수송일자'].astype(str)
df_filtered = df[df['수송일자'].str.startswith(('2023', '2024'))]

# 3. 필터링된 결과를 새로운 CSV 파일로 저장
output_filename = "서울교통공사_23_24년도_승차인원.csv"
df_filtered.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 필터링 완료! 저장된 23~24년도 행 수: {len(df_filtered)}개")
print(f"✅ 새로 생성된 파일명: {output_filename}")