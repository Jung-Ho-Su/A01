import os
import pandas as pd


def filter_automotive_companies():
    # 1. 파일이 있는 폴더 경로 설정
    # (파이참 프로젝트 폴더 내에 csv 파일들이 있다면 './' 로 둡니다)
    folder_path = '../'

    # 결과를 담을 리스트
    filtered_dataframes = []

    # 2. 필터링 키워드 설정
    # 포함할 키워드 (이 중 하나라도 포함되면 자동차 관련으로 간주)
    include_keywords = ['자동차', '차량', '승용차', '상용차', '전기차', '수소차', '오토']

    # 제외할 키워드 (포함 키워드가 있어도, 아래 단어가 포함되면 제외)
    # 예: '철도차량', '환자용 차량', '항공기', '선박' 등 필터링
    exclude_keywords = ['항공', '선박', '철도', '자전거', '환자용', '오토바이', '이륜차', '우주', '조선', '기차', '위생용', '도자기']

    # 3. 폴더 내 모든 csv 파일 탐색
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv') and '최종' not in file_name:  # 결과 파일 중복 읽기 방지
            file_path = os.path.join(folder_path, file_name)

            # 한글 인코딩 에러를 방지하기 위해 utf-8 우선 시도 후 cp949 시도
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(file_path, encoding='cp949')

            # 파일에 존재하는 컬럼 중 검사할 컬럼 지정 (업종명, 생산품)
            cols_to_check = [col for col in ['업종명', '생산품'] if col in df.columns]

            if not cols_to_check:
                print(f"건너뜀: {file_name} (검사할 컬럼이 없습니다)")
                continue

            # 문자열 검색을 위해 결측치(NaN)를 빈 문자열로 변경
            for col in cols_to_check:
                df[col] = df[col].fillna('')

            # 조건 1: 포함 키워드가 하나라도 들어있는지 확인
            include_condition = pd.Series(False, index=df.index)
            for col in cols_to_check:
                for keyword in include_keywords:
                    include_condition = include_condition | df[col].str.contains(keyword)

            # 조건 2: 제외 키워드가 하나라도 들어있는지 확인
            exclude_condition = pd.Series(False, index=df.index)
            for col in cols_to_check:
                for keyword in exclude_keywords:
                    exclude_condition = exclude_condition | df[col].str.contains(keyword)

            # 최종 조건: 포함 키워드는 있고(&) 제외 키워드는 없는(~) 행만 추출
            filtered_df = df[include_condition & ~exclude_condition].copy()

            if not filtered_df.empty:
                filtered_dataframes.append(filtered_df)
                print(f"완료: {file_name} -> {len(filtered_df)}개 기업 추출")

    # 4. 필터링된 모든 데이터를 하나의 데이터프레임으로 병합
    if filtered_dataframes:
        final_df = pd.concat(filtered_dataframes, ignore_index=True)

        # 결과를 새로운 CSV 파일로 저장 (엑셀에서 한글 깨짐 방지를 위해 utf-8-sig 사용)

        output_path = os.path.join(folder_path, '필터링_순수_자동차산업_회사목록.csv')
        final_df.to_csv(output_path, index=False, encoding='utf-8-sig')

        print(f"\n✅ 필터링 완료! 총 {len(final_df)}개의 순수 자동차 산업 기업이 추출되어 '{output_path}' 파일로 저장되었습니다.")
    else:
        print("\n조건에 맞는 자동차 산업 기업을 찾지 못했습니다.")


# 함수 실행
if __name__ == "__main__":
    filter_automotive_companies()