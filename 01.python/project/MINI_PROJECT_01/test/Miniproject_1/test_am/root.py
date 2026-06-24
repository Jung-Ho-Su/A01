import pandas as pd
import os


def filter_jeonbuk_departures():
    file_name = 'TCS_영업소간교통량_1일_1일_20260312.csv'

    if not os.path.exists(file_name):
        print(f"❌ '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return

    # 1. 파일 불러오기 (한글 인코딩 대응)
    try:
        df = pd.read_csv(file_name, encoding='utf-8-sig')
    except:
        df = pd.read_csv(file_name, encoding='cp949')

    # 2. 전처리: 컬럼명 양끝 공백 및 따옴표 제거
    df.columns = [col.strip().replace('"', '') for col in df.columns]

    # 데이터 내의 공백 제거 (검색 정확도 향상)
    df['출발영업소명'] = df['출발영업소명'].astype(str).str.strip()

    # 3. 전라북도 소재 주요 영업소 리스트 (필터링 기준)
    # 데이터 내에서 확인된 전북 지역 톨게이트 목록입니다.
    jeonbuk_offices = [
        '전주', '서전주', '동전주', '남전주', '완주', '익산', '삼례',
        '군산', '동군산', '정읍', '태인', '내장산', '김제', '북김제', '서김제',
        '부안', '줄포', '고창', '남고창', '무주', '덕유산', '진안', '장수',
        '임실', '오수', '남원', '서남원', '북남원', '동남원', '순창', '상관', '소양'
    ]

    # 4. 🎯 전라북도 출발 데이터만 필터링
    jb_df = df[df['출발영업소명'].isin(jeonbuk_offices)].copy()

    if jb_df.empty:
        print("❌ 해당 지역의 출발 데이터를 찾지 못했습니다.")
        return

    # 5. 결과 저장 (엑셀 호환을 위해 utf-8-sig 사용)
    output_filename = '전라북도_출발_영업소간_교통량.csv'
    jb_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 60)
    print(f"✅ 필터링 완료! 전북 지역 {len(jeonbuk_offices)}개 영업소의 데이터를 추출했습니다.")
    print(f"📊 추출된 데이터 수: {len(jb_df):,}건")
    print(f"💾 파일이 저장되었습니다: {output_filename}")
    print("=" * 60)

    # 상위 5개 데이터 미리보기 출력
    print("\n[추출 데이터 미리보기]")
    print(jb_df[['집계일자', '출발영업소명', '도착영업소명', '도착지방향총교통량']].head())


if __name__ == "__main__":
    filter_jeonbuk_departures()