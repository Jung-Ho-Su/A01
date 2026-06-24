import pandas as pd
import os


def extract_auto_industry_companies():
    # 처리할 파일 목록
    files = [
        "강원도 고성군_공장등록현황_20200930.csv",
        "강원도 태백시_관내 제조업 등록 공장 현황_20240814.csv",
        "강원도 홍천군_제조업 공장 현황_20201102.csv",
        "강원특별자치도 춘천시_제조업공장현황_20250206.csv",
        "강원특별자치도 홍천군_제조업 공장 등록 현황_20240923.csv"
    ]

    # 자동차 산업 관련 검색 키워드 (필요에 따라 추가/수정 가능)
    keywords = ['자동차', '차량', '부품', '모터스', '오토']

    # 정규식 패턴으로 변환 (예: '자동차|차량|부품|모터스|오토')
    search_pattern = '|'.join(keywords)

    extracted_dataframes = []

    for file in files:
        if not os.path.exists(file):
            print(f"경고: {file} 파일을 찾을 수 없습니다.")
            continue

        # 1. 파일 불러오기 (인코딩 자동 대처)
        try:
            # 먼저 utf-8로 시도
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            # 실패 시 한국 윈도우 기본 인코딩인 cp949(또는 euc-kr)로 시도
            df = pd.read_csv(file, encoding='cp949')

        print(f"[{file}] 데이터를 성공적으로 불러왔습니다. (총 {len(df)}행)")

        # 2. 데이터 분류 및 추출
        # 모든 컬럼을 문자열로 변환한 뒤, 키워드가 하나라도 포함된 행(row)을 찾음
        mask = df.astype(str).apply(lambda col: col.str.contains(search_pattern, na=False, case=False)).any(axis=1)

        # 조건에 맞는 데이터만 필터링
        filtered_df = df[mask].copy()

        if not filtered_df.empty:
            # 출처 파일을 구분하기 위해 컬럼 추가
            filtered_df['출처파일'] = file
            extracted_dataframes.append(filtered_df)

    # 3. 추출된 데이터 병합 및 저장
    if extracted_dataframes:
        # 리스트에 모인 데이터프레임들을 하나로 합치기
        final_result = pd.concat(extracted_dataframes, ignore_index=True)

        print("\n=== 🚗 자동차 산업 관련 회사 추출 결과 ===")
        print(f"총 {len(final_result)}개의 관련 회사가 검색되었습니다.")

        # 합쳐진 데이터를 확인하기 위해 상위 5개 출력
        # PyCharm 콘솔에서 컬럼이 잘리지 않게 Pandas 설정
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        print(final_result.head())

        # 결과를 새로운 CSV 파일로 저장 (엑셀에서 깨지지 않도록 utf-8-sig 사용)
        output_filename = "자동차산업_관련_회사목록.csv"
        final_result.to_csv(output_filename, index=False, encoding='utf-8-sig')
        print(f"\n데이터가 성공적으로 저장되었습니다: {output_filename}")

    else:
        print("\n자동차 산업 관련 회사를 찾을 수 없습니다.")


if __name__ == "__main__":
    # Pandas 라이브러리가 설치되어 있지 않다면 PyCharm 터미널에 아래 명령어를 입력하세요.
    # pip install pandas
    extract_auto_industry_companies()