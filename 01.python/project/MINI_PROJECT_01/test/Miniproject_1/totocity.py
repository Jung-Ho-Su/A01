import pandas as pd


def transform_to_city_summary():
    # 1. 시·군별 영업소 매핑 (사용자 제공 이미지 기준)
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

    # 매핑을 위한 역방향 사전 생성
    reverse_map = {office: city for city, offices in city_map.items() for office in offices}

    # 2. 충북 행 파일 변환
    cb_input = '전북_거점별_통합_교통량_최종(충북).csv'
    try:
        df_cb = pd.read_csv(cb_input, encoding='utf-8-sig')
        # '출발지역'을 시·군명으로 변환
        df_cb['출발_시군'] = df_cb['출발지역'].str.strip().map(reverse_map)

        # 합산할 수치 컬럼 지정
        cols_cb = ['도착지방향_교통량합계', '출발지방향_교통량합계', '전체_교통량_총합']
        for col in cols_cb:
            df_cb[col] = pd.to_numeric(df_cb[col], errors='coerce').fillna(0)

        # 시군별 그룹화 및 합산
        final_cb = df_cb.groupby('출발_시군')[cols_cb].sum().reset_index()
        final_cb.to_csv('전북_시군별_충북_통합_교통량.csv', index=False, encoding='utf-8-sig')
        print(f"✅ '{cb_input}' -> '전북_시군별_충북_통합_교통량.csv' 변환 완료")
    except Exception as e:
        print(f"❌ 충북 파일 처리 중 오류: {e}")

    # 3. 수도권 행 파일 변환
    met_input = '전북_지역별_통합_교통량(수도권).csv'
    try:
        df_met = pd.read_csv(met_input, encoding='utf-8-sig')
        df_met['출발_시군'] = df_met['출발지역'].str.strip().map(reverse_map)

        cols_met = ['도착지방향총교통량', '출발지방향총교통량']
        for col in cols_met:
            df_met[col] = pd.to_numeric(df_met[col], errors='coerce').fillna(0)

        # 시군별 그룹화 및 합산
        final_met = df_met.groupby('출발_시군')[cols_met].sum().reset_index()
        # 전체 총합 컬럼 추가
        final_met['전체_교통량_총합'] = final_met['도착지방향총교통량'] + final_met['출발지방향총교통량']
        final_met.to_csv('전북_시군별_수도권_통합_교통량.csv', index=False, encoding='utf-8-sig')
        print(f"✅ '{met_input}' -> '전북_시군별_수도권_통합_교통량.csv' 변환 완료")
    except Exception as e:
        print(f"❌ 수도권 파일 처리 중 오류: {e}")


if __name__ == "__main__":
    transform_to_city_summary()