import pandas as pd
import os


def aggregate_jeonbuk_to_chungnam():
    # 1. 파일 불러오기
    input_file = '전북출발_충남도착_교통량_계산완료.csv'

    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' 파일을 찾을 수 없습니다.")
        return

    try:
        df = pd.read_csv(input_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(input_file, encoding='cp949')

    # 컬럼명 및 데이터 정제 (따옴표 제거 등)
    df.columns = [col.strip().replace('"', '') for col in df.columns]

    # 2. 🗺️ 이미지 기반 전북 시·군별 영업소 매핑 사전
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

    # 영업소명을 시·군명으로 변환하기 위한 역매핑용 딕셔너리
    reverse_map = {office: city for city, offices in city_map.items() for office in offices}

    # 3. '출발영업소명'을 '출발_시군'으로 매핑
    df['출발_시군'] = df['출발영업소명'].str.strip().map(reverse_map)

    # 4. 🎯 데이터 통합 (GroupBy)
    # 수치형 데이터 컬럼(교통량 및 합계) 추출
    # 이전 단계에서 만든 '교통량합계', '전체_교통량_총합' 등도 모두 포함됩니다.
    traffic_cols = [col for col in df.columns if '교통량' in col or '합계' in col or '총합' in col]

    # 숫자형으로 확실히 변환 (에러 방지)
    for col in traffic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 시·군별로 그룹화하여 합계 계산
    # (도착지는 이미 충남으로 한정되어 있으므로 출발 시군 기준으로만 묶습니다.)
    final_df = df.groupby('출발_시군')[traffic_cols].sum().reset_index()

    # 5. 결과 저장
    output_filename = '전북_시군별_충남도착_통합_교통량.csv'
    final_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 70)
    print(f"✅ 전북 시·군 → 충남 도착 데이터 통합 완료!")
    print(f"📊 통합된 시·군 수: {len(final_df)}개")
    print(f"💾 최종 결과 파일: {output_filename}")
    print("=" * 70)

    # 결과 상위 데이터 미리보기
    print(final_df.head(10))


if __name__ == "__main__":
    aggregate_jeonbuk_to_chungnam()