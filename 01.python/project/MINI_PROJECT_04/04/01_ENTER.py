import pandas as pd
import os

# 1. 파일 설정
file_name = '주요관광지점 입장객(2023~2025).csv'
current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, file_name)

if not os.path.exists(file_path):
    file_path = file_name


def load_data(path):
    """파일을 안전하게 읽어오는 함수"""
    for enc in ['cp949', 'utf-8', 'euc-kr']:
        try:
            return pd.read_csv(path, header=[0, 1], encoding=enc)
        except:
            continue
    return None


try:
    df = load_data(file_path)
    if df is None: raise Exception("파일을 읽을 수 없습니다.")

    # 2. 데이터 전처리 (콤마 제거 및 숫자 변환)
    # 인원계 및 월별 데이터 모두 숫자형으로 변환
    years = ['2023년', '2024년', '2025년']
    for year in years:
        cols = [c for c in df.columns if c[0] == year]
        for col in cols:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce').fillna(0)

    # 전체 통합 합계 계산 (3개년 인원계 합산)
    df[('통합', '3개년합계')] = df[('2023년', '인원계')] + df[('2024년', '인원계')] + df[('2025년', '인원계')]

    # 3. 중복 방지 및 Top 5 선정 로직
    # '내/외국인' 구분 컬럼이 '합계'인 행만 추출 (관광지 중복 방지의 핵심)
    # 컬럼 위치가 인덱스 3번 (내/외국인)임을 확인
    type_col = df.columns[3]
    name_col = df.columns[2]  # 관광지명 컬럼

    # 합계 행만 골라내어 전체 순위 산출
    total_rows = df[df[type_col] == '합계'].copy()
    top5_names = total_rows.sort_values(by=('통합', '3개년합계'), ascending=False).head(5)[name_col].tolist()

    print(f"🏆 선정된 Top 5 관광지: {top5_names}")

    # 4. 선정된 관광지의 모든 행(내국인, 외국인, 합계) 추출
    # 선정된 관광지 리스트에 포함된 행들만 필터링
    final_top5_detail = df[df[name_col].isin(top5_names)].copy()

    # 보기 좋게 관광지명과 합계순으로 정렬
    # '통합 3개년합계'를 모든 행에 부여하기 위해 매핑 후 정렬
    rank_map = {name: i for i, name in enumerate(top5_names)}
    final_top5_detail['순위'] = final_top5_detail[name_col].map(rank_map)
    final_top5_detail = final_top5_detail.sort_values(by=['순위', type_col])

    # 순위 임시 컬럼 삭제
    final_top5_detail = final_top5_detail.drop(columns=['순위'])

    # 5. 결과 저장
    output_name = 'Top5_관광지_상세내역(중복제거).csv'
    final_top5_detail.to_csv(output_name, index=False, encoding='utf-8-sig')

    print(f"✅ 결과가 성공적으로 저장되었습니다: {output_name}")
    print(final_top5_detail[[name_col, type_col, ('통합', '3개년합계')]].head(15))  # 결과 요약 출력

except Exception as e:
    print(f"❌ 오류 발생: {e}")