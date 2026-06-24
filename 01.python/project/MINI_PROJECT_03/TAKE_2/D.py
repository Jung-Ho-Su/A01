import pandas as pd

# 1. 이전 단계에서 생성한 '총 이용객수(승차+하차)' 파일 불러오기
file_path = "서울교통공사_23년도_총이용객수(승차+하차).csv"

# 인코딩 처리 (한글 깨짐 방지)
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp949')

print("✅ 데이터를 불러왔습니다. 전체 합산 작업을 시작합니다...")

# 2. 합산할 시간대 컬럼 리스트 추출 ('시' 글자가 포함된 모든 컬럼)
time_cols = [col for col in df.columns if '시' in col]

# 3. 모든 행의 시간대별 인원수를 수직으로 다 더하기 (Column-wise Sum)
# 이 작업으로 모든 역, 모든 날짜의 데이터가 시간대별로 단 하나의 합계 값이 됩니다.
total_sum = df[time_cols].sum()

# 4. 합산된 결과를 새로운 데이터프레임(1개 행)으로 변환
# 기존 '역명', '호선' 등의 정보는 전체 합계이므로 '2023년 전체 총합'으로 표시합니다.
result_df = pd.DataFrame([total_sum])
result_df.insert(0, '구분', '2023년 전체 총합')

# 5. 최종 결과를 CSV 파일로 저장
output_file = "서울교통공사_23년도_시간대별_전체총합.csv"
result_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 합산 완료! 2023년 전체 이용객 요약 파일이 생성되었습니다: {output_file}")
print(result_df)