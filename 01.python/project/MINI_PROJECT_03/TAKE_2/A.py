import pandas as pd

# 1. 원본 데이터 불러오기 (23년도 파일)
file_path = "서울교통공사_역별 시간대별 승하차인원(23.1~23.12).csv"

try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='utf-8')

print("✅ 데이터 로딩 완료! 승하차 차이 계산을 시작합니다...")

# 2. 데이터를 묶을 공통 기준열(Key) 설정
keys = ['수송일자', '호선', '역번호', '역명']

# 3. 시간대 컬럼만 추출 ('시'라는 글자가 포함된 컬럼)
time_cols = [col for col in df.columns if '시' in col and col != '승하차구분']

# 4. 승차 데이터와 하차 데이터를 분리한 후, 공통 기준열을 인덱스(Index)로 설정
# 이렇게 하면 각 역의 시간대 데이터가 정확히 같은 줄(Row)에 위치하게 됩니다.
df_in = df[df['승하차구분'] == '승차'].set_index(keys)[time_cols]
df_out = df[df['승하차구분'] == '하차'].set_index(keys)[time_cols]

# 5. 시간대별로 (승차 - 하차) 계산 수행
# fill_value=0 을 넣어 결측치로 인한 에러를 방지합니다.
df_diff = df_in.sub(df_out, fill_value=0)

# 6. 인덱스로 만들었던 기준열들을 다시 일반 컬럼으로 꺼내기
df_diff = df_diff.reset_index()

# 7. 새로운 CSV 파일로 저장
output_file = "서울교통공사_23년도_순승차인원(승차-하차).csv"
df_diff.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 원본 행 수: {len(df)}개")
print(f"✅ 계산 후 행 수: {len(df_diff)}개 (정확히 절반으로 병합됨)")
print(f"✅ 새로 생성된 파일명: {output_file}")