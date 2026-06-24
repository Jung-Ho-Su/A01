import pandas as pd

# 1. '23년도 승차 인원만 추출'한 파일 불러오기
file_path = "서울교통공사_23년도_승차인원만_추출.csv"

# 인코딩 처리 (한글 깨짐 방지)
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

print("✅ 데이터를 불러왔습니다. 승차 인원 전체 합산 작업을 시작합니다...")

# 2. 합산할 시간대 컬럼 리스트 추출 ('시' 글자가 포함된 컬럼 중 '승하차구분' 또는 '구분' 제외)
# 23년도는 보통 '승하차구분', 24년도는 '구분'을 사용하므로 둘 다 제외 조건에 넣었습니다.
time_cols = [col for col in df.columns if '시' in col and col not in ['승하차구분', '구분']]

# 3. 모든 행의 시간대별 승차 인원을 수직으로 다 더하기 (Column-wise Sum)
total_sum = df[time_cols].sum()

# 4. 합산된 결과를 새로운 데이터프레임(1개 행)으로 변환
result_df = pd.DataFrame([total_sum])
result_df.insert(0, '구분', '2023년 전체 승차 총합')

# 5. 최종 결과를 CSV 파일로 저장
output_file = "서울교통공사_23년도_승차시간별_전체총합.csv"
result_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 합산 완료! 2023년 전체 승차 인원 요약 파일이 생성되었습니다: {output_file}")