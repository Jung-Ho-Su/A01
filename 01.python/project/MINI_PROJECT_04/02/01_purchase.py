import pandas as pd
import matplotlib.pyplot as plt
import glob

# 폰트 설정 (한글 깨짐 방지용)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# --- 예시 데이터 설정 (이전 정보 바탕으로 재구성, 실제 데이터 사용시 수정 필요) ---
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']

# 전시회 개수 (붉은 점선, 우측 Y축) - 이전 데이터에서 추출
exhib_counts = [3, 4, 10, 5, 9, 6, 8, 14, 9, 12, 9, 6]

# 상권 소비액 (푸른 실선, 좌측 Y축) - 그래프 이미지에서 대략적으로 추정한 예시 데이터
# (단위: 천원, 실제 데이터와 다를 수 있으므로 개념 확인용으로만 사용)
commercial_spend = [39000000, 39500000, 41000000, 44000000, 47000000, 45500000, 47500000, 45000000, 41500000, 39000000, 37500000, 41000000]

# 숙박 소비액 (초록 실선, 좌측 Y축) - 그래프 이미지에서 대략적으로 추정한 예시 데이터
# (단위: 천원, 실제 데이터와 다를 수 있으므로 개념 확인용으로만 사용)
accommodation_spend = [20000000, 20500000, 24000000, 26500000, 29500000, 27000000, 29000000, 27500000, 24500000, 22500000, 19500000, 23000000]
# --------------------------------------------------------------------------------------


# --- 그래프 1: 전시회 개수 vs 상권 소비 추이 ---
# 새로운 그래프 창 생성 (plt.figure() 사용)
fig1, ax1_1 = plt.subplots(figsize=(10, 6))

# 왼쪽 Y축: 상권 소비액 실선 그래프 그리기
ax1_1.plot(months, commercial_spend, marker='o', label='상권 소비액', color='blue')
ax1_1.set_xlabel('월')
ax1_1.set_ylabel('상권 소비액 (천원)', color='blue')
ax1_1.tick_params(axis='y', labelcolor='blue')

# 오른쪽 Y축 (twinx): 전시회 개수 점선 그래프 그리기
ax1_2 = ax1_1.twinx()
ax1_2.plot(months, exhib_counts, linestyle='--', marker='^', color='red', label='전시회 개수')
ax1_2.set_ylabel('전시회 개수 (건)', color='red')
ax1_2.tick_params(axis='y', labelcolor='red')

# 제목 및 범례 설정
plt.title('2023년 송도 전시회 개최 현황 및 상권 소비 추이 비교')
# 두 Y축의 범례를 합쳐서 표시하기 위한 처리
lines1_1, labels1_1 = ax1_1.get_legend_handles_labels()
lines1_2, labels1_2 = ax1_2.get_legend_handles_labels()
ax1_1.legend(lines1_1 + lines1_2, labels1_1 + labels1_2, loc='upper left')

# 그래프 출력
plt.tight_layout()
# 첫 번째 그래프 표시 (실행 환경에 따라 창이 즉시 나타남)
plt.show()


# --- 그래프 2: 전시회 개수 vs 숙박 소비 추이 ---
# 새로운 그래프 창 생성
fig2, ax2_1 = plt.subplots(figsize=(10, 6))

# 왼쪽 Y축: 숙박 소비액 실선 그래프 그리기
ax2_1.plot(months, accommodation_spend, marker='s', label='숙박 소비액', color='green')
ax2_1.set_xlabel('월')
ax2_1.set_ylabel('숙박 소비액 (천원)', color='green')
ax2_1.tick_params(axis='y', labelcolor='green')

# 오른쪽 Y축 (twinx): 전시회 개수 점선 그래프 그리기
ax2_2 = ax2_1.twinx()
ax2_2.plot(months, exhib_counts, linestyle='--', marker='^', color='red', label='전시회 개수')
ax2_2.set_ylabel('전시회 개수 (건)', color='red')
ax2_2.tick_params(axis='y', labelcolor='red')

# 제목 및 범례 설정
plt.title('2023년 송도 전시회 개최 현황 및 숙박 소비 추이 비교')
# 두 Y축의 범례를 합쳐서 표시하기 위한 처리
lines2_1, labels2_1 = ax2_1.get_legend_handles_labels()
lines2_2, labels2_2 = ax2_2.get_legend_handles_labels()
ax2_1.legend(lines2_1 + lines2_2, labels2_1 + labels2_2, loc='upper left')

# 그래프 출력
plt.tight_layout()
# 두 번째 그래프 표시
plt.show()