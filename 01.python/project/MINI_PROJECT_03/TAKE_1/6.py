import pandas as pd

# 1. 합칠 파일 이름 지정 (파일이 파이썬 스크립트와 같은 폴더에 있어야 합니다)
file_23 = "23년도_추정혼잡도(%).csv"
file_24 = "24년도_추정혼잡도(%).csv"

# 2. 데이터 불러오기 (인코딩 에러 방지 처리)
def load_csv(file_name):
    try:
        return pd.read_csv(file_name, encoding='utf-8-sig')
    except UnicodeDecodeError:
        try:
            return pd.read_csv(file_name, encoding='cp949')
        except:
            return pd.read_csv(file_name, encoding='utf-8')

print("✅ 데이터를 불러오는 중입니다...")
df_23 = load_csv(file_23)
df_24 = load_csv(file_24)

print(f"✔️ 23년도 데이터 행 수: {len(df_23):,}개")
print(f"✔️ 24년도 데이터 행 수: {len(df_24):,}개")

# 3. 데이터 위아래로 합치기 (Concat)
# ignore_index=True를 설정해야 기존 인덱스가 꼬이지 않고 0부터 순서대로 새로 매겨집니다.
df_combined = pd.concat([df_23, df_24], ignore_index=True)

# 4. 합쳐진 데이터를 새로운 CSV 파일로 저장
output_file = "23_24년도_통합_추정혼잡도.csv"
df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ 통합 완료! 총 데이터 행 수: {len(df_combined):,}개")
print(f"✅ 새로 생성된 파일명: {output_file}")