import pandas as pd

# 1. 원본 데이터 불러오기 (23년도 파일)
file_path = "서울교통공사_역별 시간대별 승하차인원(23.1~23.12).csv"

# 인코딩 처리
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except:
        df = pd.read_csv(file_path, encoding='utf-8-sig')

print("✅ 데이터 로딩 완료! 승하차 인원 합산을 시작합니다...")

# 2. 데이터를 하나로 묶을 공통 기준열(Key) 설정
keys = ['수송일자', '호선', '역번호', '역명']

# 3. 계산을 수행할 시간대 컬럼만 추출 ('시'가 포함된 컬럼)
time_cols = [col for col in df.columns if '시' in col and col != '승하차구분']

# 4. 공통 기준열을 바탕으로 그룹화(groupby)한 뒤, 시간대별 숫자를 모두 더하기(sum)
# 이 한 줄의 코드로 같은 날짜/호선/역명의 '승차'와 '하차' 행이 하나로 합산됩니다.
df_sum = df.groupby(keys)[time_cols].sum().reset_index()

# 5. 합산된 결과를 새로운 CSV 파일로 저장
output_file = "서울교통공사_23년도_총이용객수(승차+하차).csv"
df_sum.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 원본 행 수: {len(df)}개")
print(f"✅ 승하차 합계 후 행 수: {len(df_sum)}개 (하나의 행으로 병합됨)")
print(f"✅ 새로 생성된 파일명: {output_file}")