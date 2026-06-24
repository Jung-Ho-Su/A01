import pandas as pd
import numpy as np

# 1. 2024년 엑셀 원본 파일 불러오기
# (파일 상단의 제목 두 줄을 건너뛰기 위해 skiprows=2 사용)
file_name = '송도컨벤시아 행사일정(2024).xlsx'
df = pd.read_excel(file_name, skiprows=2)

# 2. '기간' 컬럼을 시작일과 종료일로 분리 ('2024-01-20 ~ 2024-01-21' 형태)
# expand=True를 사용하여 두 개의 컬럼으로 나눕니다.
df[['시작일', '종료일']] = df['기간'].str.split(' ~ ', expand=True)

# 3. 날짜 데이터로 변환 (텍스트 형식을 계산 가능한 날짜 형식으로 변환)
df['시작일'] = pd.to_datetime(df['시작일'])
df['종료일'] = pd.to_datetime(df['종료일'])

# 4. 개최월 및 개최일수 계산
df['개최월'] = df['시작일'].dt.month
df['개최일수'] = (df['종료일'] - df['시작일']).dt.days + 1

# 5. 결과를 담을 딕셔너리 준비
result_dict = {}

# [월별 데이터 추출] 1월 ~ 12월 컬럼 생성
for i in range(1, 13):
    # 해당 월에 시작하는 행사명 중 중복 제거 리스트
    names = df[df['개최월'] == i]['행사명'].dropna().unique().tolist()
    count = len(names)
    # 첫 행은 개수, 그 아래는 행사명들이 오도록 구성
    result_dict[f'{i}월'] = [count] + names

# [기간별 데이터 추출] N일 개최 건수 컬럼 생성
# 실제 데이터에 존재하는 개최 일수만 찾아 오름차순으로 정리
durations = sorted(df['개최일수'].dropna().unique())
for d in durations:
    names = df[df['개최일수'] == d]['행사명'].dropna().unique().tolist()
    count = len(names)
    result_dict[f'{int(d)}일 개최 건수'] = [count] + names

# 6. 모든 컬럼의 길이를 가장 긴 컬럼에 맞춰 빈칸(NaN)으로 채우기
# (데이터프레임 생성 시 모든 열의 행 개수가 같아야 하기 때문입니다)
max_len = max(len(v) for v in result_dict.values())
for k in result_dict.keys():
    result_dict[k] += [np.nan] * (max_len - len(result_dict[k]))

# 7. 데이터프레임으로 변환 후 요약 CSV 파일로 저장
final_df = pd.DataFrame(result_dict)
output_filename = '2024년도 전시회 요약.csv'

# 한글 깨짐 방지를 위해 'utf-8-sig' 인코딩 사용
final_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 작업 완료! '{output_filename}' 파일이 성공적으로 생성되었습니다.")