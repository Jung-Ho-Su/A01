import pandas as pd

# 1. 파일 불러오기 (이전 단계에서 만든 순승차인원 파일)
file_path = "서울교통공사_23년도_순승차인원(승차-하차).csv"

# 인코딩 처리 (한글 깨짐 방지)
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='cp949')
    except:
        df = pd.read_csv(file_path, encoding='utf-8')

print("✅ 데이터 로딩 완료! 출퇴근 시간대 필터링을 시작합니다...")

# 2. 남기고 싶은 컬럼 리스트 지정
# 기본 정보(날짜, 호선, 역번호, 역명)와 목표 시간대만 선택합니다.
# 17-18시간대 = 오후 5~6시 / 18-19시간대 = 오후 6~7시
target_columns = [
    '수송일자', '호선', '역번호', '역명',
    '07-08시간대', '08-09시간대',
    '17-18시간대', '18-19시간대'
]

# 3. 지정한 컬럼만 포함되도록 데이터프레임 자르기
df_filtered = df[target_columns]

# 4. 새로운 CSV 파일로 저장
output_file = "서울교통공사_23년도_출퇴근시간_순승차인원.csv"
df_filtered.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 추출 완료! 다른 시간대 컬럼은 삭제되었습니다.")
print(f"✅ 새로 생성된 파일명: {output_file}")