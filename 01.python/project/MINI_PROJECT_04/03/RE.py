import pandas as pd

# 1. 데이터 불러오기
file_path = 'incheon_filtered_data_2023.csv'
df = pd.read_csv(file_path)

# 모든 컬럼명의 앞뒤 공백 제거 (KeyError 예방)
df.columns = df.columns.str.strip()

# 2. 합산할 대상 컬럼 설정
# 이미지에 있던 주요 수치 컬럼들입니다.
target_cols = ['PRFPLC_CO', 'FOOD_FCL', 'LDGMNT_I', 'POPLTN_C']

# [중요] 실제 파일에 존재하는 컬럼만 필터링 (에러 방지)
existing_target_cols = [col for col in target_cols if col in df.columns]

print(f"합산에 사용될 컬럼: {existing_target_cols}")

# 3. 'SIGNGU_NM' 기준으로 그룹화하여 합계 계산
if 'SIGNGU_NM' in df.columns:
    # 수치형 데이터만 합산하도록 설정
    df_summed = df.groupby('SIGNGU_NM')[existing_target_cols].sum().reset_index()

    # 4. 결과 저장
    output_file = 'incheon_gu_summary_2023.csv'
    df_summed.to_csv(output_file, index=False, encoding='utf-8-sig')

    print("\n--- 처리 완료 ---")
    print(df_summed)
    print(f"\n성공적으로 '{output_file}' 파일이 생성되었습니다.")
else:
    print("오류: 파일에서 'SIGNGU_NM' 컬럼을 찾을 수 없습니다.")
    print(f"현재 파일 컬럼 목록: {df.columns.tolist()}")
