import pandas as pd


def transform_metropolitan_to_city():
    # 1. 시·군별 영업소 매핑 사전 (이미지 기준)
    city_map = {
        '전주시': ['전주', '서전주', '동전주', '남전주'],
        '익산시': ['익산', '삼례'],
        '군산시': ['군산', '동군산'],
        '정읍시': ['정읍', '태인', '내장산'],
        '김제시': ['김제', '북김제', '서김제'],
        '남원시': ['남원', '서남원', '북남원', '동남원'],
        '완주군': ['완주', '상관', '소양'],
        '무주군': ['무주', '덕유산'],
        '진안군': ['진안'],
        '장수군': ['장수'],
        '임실군': ['임실', '오수'],
        '순창군': ['순창'],
        '고창군': ['고창', '남고창', '선운사'],
        '부안군': ['부안', '줄포']
    }

    # 역매핑용 딕셔너리 생성
    reverse_map = {office: city for city, offices in city_map.items() for office in offices}

    # 2. 수도권 파일 불러오기
    input_file = '전북_지역별_통합_교통량(수도권).csv'
    try:
        df = pd.read_csv(input_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(input_file, encoding='cp949')

    # 3. '출발지역' 컬럼을 시·군명으로 변환
    df['출발_시군'] = df['출발지역'].str.strip().map(reverse_map)

    # 4. 수치형 데이터 정제 및 통합 계산
    target_cols = ['도착지방향총교통량', '출발지방향총교통량']
    for col in target_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 시군별 그룹화 및 합산
    final_df = df.groupby('출발_시군')[target_cols].sum().reset_index()

    # 타 지역 파일과 형식을 맞추기 위해 전체 총합 컬럼 추가
    final_df['전체_교통량_총합'] = final_df['도착지방향총교통량'] + final_df['출발지방향총교통량']

    # 5. 결과 저장
    output_name = '전북_시군별_수도권_통합_교통량.csv'
    final_df.to_csv(output_name, index=False, encoding='utf-8-sig')

    print("=" * 60)
    print(f"✅ 변환 완료! '{output_name}' 파일이 생성되었습니다.")
    print("=" * 60)
    print(final_df.head())


if __name__ == "__main__":
    transform_metropolitan_to_city()