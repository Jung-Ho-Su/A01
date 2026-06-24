import pandas as pd
import numpy as np

# 1. 파일 불러오기 (이전 단계에서 만든 파일)
file_path = "서울교통공사_23_24년도_승차인원.csv"

try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='cp949')
    except:
        df = pd.read_csv(file_path, encoding='utf-8')

print("✅ 데이터 로딩 완료! 혼잡도 계산을 시작합니다...")

# 2. 이미지 기반: 호선별 칸수(량수) 매핑 딕셔너리
car_counts = {
    '1호선': 10, '2호선': 10, '3호선': 10, '4호선': 10,
    '5호선': 8, '6호선': 8, '7호선': 8, '8호선': 6,
    '9호선': 6 # 9호선 데이터가 있을 경우를 대비해 추가
}

# 텍스트 공백 등 오류 방지를 위해 양옆 공백 제거 후 칸수 매핑
df['호선_정제'] = df['호선'].astype(str).str.strip()
df['칸수'] = df['호선_정제'].map(car_counts)

# 혹시 데이터에 딕셔너리에 없는 호선(예: 우이신설선 등)이 있다면 제외하거나 기본값(예: 2량) 처리
df = df.dropna(subset=['칸수']) # 계산 불가능한 노선은 안전하게 제외

# 3. 시간대 컬럼들만 추출 (컬럼명에 '시'가 포함된 열을 찾음)
# 이전 데이터 기준 ['06시이전', '06-07시간대', '07-08시간대' ...]
time_cols = [col for col in df.columns if '시' in col and col != '승하차구분']

# 4. 혼잡도 계산하여 기존 컬럼에 덮어쓰기
# 공식: (해당 시간대 승차인원 / (160 * 해당 호선의 칸수)) * 100
for col in time_cols:
    # 계산 후 소수점 첫째 자리까지만 깔끔하게 남깁니다.
    df[col] = ((df[col] / (160 * df['칸수'])) * 100).round(1)

# 5. 계산용으로 만든 임시 컬럼 삭제 및 최종 파일 저장
df = df.drop(columns=['호선_정제', '칸수'])

output_filename = "서울교통공사_시간대별_추정혼잡도(%).csv"
df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 혼잡도 퍼센트(%) 변환 완료! 새로 생성된 파일명: {output_filename}")