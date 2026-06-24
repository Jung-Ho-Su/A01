import pandas as pd


def remove_unrelated_companies():
    # 1. 기존에 생성된 파일 불러오기
    file_path = '필터링_순수_자동차산업_회사목록.csv'

    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    # 2. 추가로 제외할 2차 필터링 키워드 목록
    # 주차, 도로 인프라, 보안 카메라, 장난감, 세차 등 자동차 제조와 거리가 먼 키워드들
    extra_exclude_keywords = [
        '전광판', 'CCTV', '영상감시', '출입통제', '속도측정기', '무인교통', '무인안내', '정보안내장치',
        '차량번호', '차량인식', '판독기', '차단기', '정산기', '발권기', '주차관제', '주차요금',
        '주차제어', '주차안내', '신호장치', '신호기', '보안용', '장난감', '유모차', '휠체어',
        '방향제', '세차', '도로명판', '표지판', '건물번호판'
    ]

    # 결측치(NaN)를 빈 문자열로 처리하여 에러 방지
    df['업종명'] = df['업종명'].fillna('').astype(str)
    df['생산품'] = df['생산품'].fillna('').astype(str)

    # 3. 추가 제외 키워드가 포함된 행 찾기 (정규표현식 활용)
    # 업종명이나 생산품 둘 중 하나라도 제외 키워드가 포함되어 있으면 True 반환
    mask = (
            df['생산품'].str.contains('|'.join(extra_exclude_keywords)) |
            df['업종명'].str.contains('|'.join(extra_exclude_keywords))
    )

    # 제외 키워드가 없는 순수 자동차 산업 데이터만 추출 (~mask)
    final_df = df[~mask].copy()

    # 어떤 회사들이 제외되었는지 확인하기 위한 데이터 (선택사항)
    removed_df = df[mask].copy()

    # 4. 최종 결과 파일 저장
    output_path = '최종_순수_자동차산업_회사목록.csv'
    final_df.to_csv(output_path, index=False, encoding='utf-8-sig')

    # (선택) 걸러진 비관련 데이터들을 따로 보고 싶다면 파일로 저장해둡니다.
    removed_df.to_csv('제외된_비관련_회사목록.csv', index=False, encoding='utf-8-sig')

    print("=== 2차 정밀 필터링 완료 ===")
    print(f"- 기존 데이터 수: {len(df)}개")
    print(f"- 제외된 비관련 기업 수: {len(removed_df)}개")
    print(f"👉 최종 순수 자동차 관련 기업 수: {len(final_df)}개")
    print(f"\n✅ 순수 자동차 회사 목록이 '{output_path}' 파일로 저장되었습니다.")
    print(f"✅ (참고) 제외된 목록은 '제외된_비관련_회사목록.csv'에서 확인하실 수 있습니다.")


if __name__ == "__main__":
    remove_unrelated_companies()
