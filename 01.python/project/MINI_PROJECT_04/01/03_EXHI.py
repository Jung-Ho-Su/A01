import pandas as pd
import numpy as np

# 1. 2025년 엑셀 원본 파일 불러오기
# 파일 상단의 제목 두 줄을 무시하기 위해 skiprows=2를 사용합니다.
file_name = '송도컨벤시아 행사일정(2025).xlsx'
df = pd.read_excel(file_name, skiprows=2)

# 2. '기간' 컬럼을 시작일과 종료일로 분리
df[['시작일', '종료일']] = df['기간'].str.split(' ~ ', expand=True)

# 3. 날짜 데이터로 변환 (텍스트 데이터를 실제 날짜 객체로 변경)
df['시작일'] = pd.to_datetime(df['시작일'])
df['종료일'] = pd.to_datetime(df['종료일'])

# 4. 개최월 및 개최일수 계산
df['개최월'] = df['시작일'].dt.month
df['개최일수'] = (df['종료일'] - df['시작일']).dt.days + 1

# 5. 결과를 담을 빈 딕셔너리 준비
result_dict = {}

# [월별 데이터 추출] 1월부터 12월까지 순회
for i in range(1, 13):
    # 해당 월에 시작하는 행사명 추출 (중복 제거)
    names = df[df['개최월'] == i]['행사명'].dropna().unique().tolist()
    count = len(names)
    # 첫 번째 칸에는 개수를, 그 아래로는 행사명 리스트를 합칩니다.
    result_dict[f'{i}월'] = [count] + names

# [기간별 데이터 추출] 개최 일수별로 분류
# 데이터에 있는 개최 일수들을 오름차순으로 정렬하여 가져옵니다.
durations = sorted(df['개최일수'].dropna().unique())
for d in durations:
    names = df[df['개최일수'] == d]['행사명'].dropna().unique().tolist()
    count = len(names)
    result_dict[f'{int(d)}일 개최 건수'] = [count] + names

# 6. 컬럼마다 데이터 개수가 다르므로 빈 공간을 NaN(빈칸)으로 채워 길이를 맞춥니다.
max_len = max(len(v) for v in result_dict.values())
for k in result_dict.keys():
    result_dict[k] += [np.nan] * (max_len - len(result_dict[k]))

# 7. 데이터프레임으로 변환 후 CSV 파일로 저장
final_df = pd.DataFrame(result_dict)
output_filename = '2025년도 전시회 요약.csv'

# 한글 깨짐 방지를 위해 'utf-8-sig' 인코딩을 사용합니다.
final_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"✅ 작업 완료! '{output_filename}' 파일이 성공적으로 생성되었습니다.")