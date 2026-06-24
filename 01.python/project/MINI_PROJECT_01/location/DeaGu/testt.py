import pandas as pd
import os


def extract_daegu_auto_companies():
    # 1. 처리할 대구광역시 4개 파일 목록
    files = [
        "대구광역시 군위군_제조업현황_20220905.csv",
        "대구광역시 서구_공장등록 현황_20251110.csv",
        "대구광역시_산업단지 기업 등록현황_20250707.csv",
        "대구광역시_제조업체(공장등록업체)현황_20250707.csv"
    ]

    # 검색 키워드
    keywords = ['자동차', '차량', '부품', '모터스', '오토']
    search_pattern = '|'.join(keywords)

    extracted_dataframes = []

    for file in files:
        if not os.path.exists(file):
            print(f"경고: [{file}] 파일을 찾을 수 없습니다.")
            continue

        # 2. 파일 불러오기 (인코딩 자동 대처)
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file, encoding='cp949')
            except Exception as e:
                print(f"오류: [{file}] 파일을 읽을 수 없습니다. ({e})")
                continue

        # 3. 데이터 필터링 (모든 컬럼을 텍스트로 변환 후 키워드 검색)
        mask = df.astype(str).apply(lambda col: col.str.contains(search_pattern, na=False, case=False)).any(axis=1)
        filtered_df = df[mask].copy()

        if not filtered_df.empty:
            # 4. 대구 지자체별로 제각각인 컬럼명을 공통 컬럼명으로 통일

            # [회사명] 통일
            company_cols = ['회사명', '업체명', '상호명']
            filtered_df['통합_회사명'] = ""
            for col in company_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_회사명'] = filtered_df['통합_회사명'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [업종명] 통일
            industry_cols = ['업종명', '업종구분', '업종']
            filtered_df['통합_업종명'] = ""
            for col in industry_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_업종명'] = filtered_df['통합_업종명'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [생산품] 통일
            prod_cols = ['생산품', '생산품목', '주요생산품명', '주력사업(생산품)', '주력생산품']
            filtered_df['통합_생산품'] = ""
            for col in prod_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_생산품'] = filtered_df['통합_생산품'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [주소] 통일 ('공장대표주소(도로명)', '도로명주소', '주소', '공장대표주소' 등)
            addr_cols = ['공장대표주소(도로명)', '도로명주소', '주소', '공장대표주소', '소재지주소', '공장대표주소(지번)']
            filtered_df['통합_주소'] = ""
            for col in addr_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_주소'] = filtered_df['통합_주소'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [연락처] 통일
            tel_cols = ['전화번호', '연락처']
            filtered_df['통합_연락처'] = ""
            for col in tel_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_연락처'] = filtered_df['통합_연락처'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [출처파일] 기록
            filtered_df['출처파일'] = file

            # 5. 통일된 핵심 컬럼만 잘라내기
            final_cols = ['통합_회사명', '통합_업종명', '통합_생산품', '통합_주소', '통합_연락처', '출처파일']

            # 누락된 컬럼이 있을 경우를 대비하여 빈 열 생성 (예: 서구 파일은 업종명 컬럼이 없음)
            for col in final_cols:
                if col not in filtered_df.columns:
                    filtered_df[col] = ""

            clean_df = filtered_df[final_cols].rename(columns={
                '통합_회사명': '회사명',
                '통합_업종명': '업종명',
                '통합_생산품': '생산품',
                '통합_주소': '주소',
                '통합_연락처': '연락처'
            })

            extracted_dataframes.append(clean_df)
            print(f"✔️ [{file}] 추출 완료: {len(clean_df)}건의 관련 회사 발견")

    # 6. 최종 데이터를 병합하여 CSV 파일로 저장
    if extracted_dataframes:
        # 데이터프레임 병합 및 빈 값(NaN) 처리
        final_result = pd.concat(extracted_dataframes, ignore_index=True).fillna("")

        # 중복 데이터 제거 (회사명과 주소가 동일한 데이터가 중복으로 존재할 경우 첫 번째 항목만 남김)
        # ※ 대구광역시 산업단지 파일과 제조업체 현황 파일의 내용이 많이 겹칠 수 있으므로 매우 유용합니다.
        final_result = final_result.drop_duplicates(subset=['회사명', '주소'], keep='first')

        # 저장할 파일명 지정
        output_file = "대구광역시_자동차산업_관련_회사목록_통합본.csv"

        # 엑셀에서 바로 열어도 한글이 깨지지 않도록 utf-8-sig 인코딩으로 저장
        final_result.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"\n✅ 작업 완료! 중복 제거 후 총 {len(final_result)}개의 데이터가 병합되어 저장되었습니다.")
        print(f"👉 파일명: {output_file} (엑셀에서 더블클릭하여 바로 확인 가능합니다)")
    else:
        print("\n자동차 산업 관련 회사를 찾을 수 없습니다.")


if __name__ == "__main__":
    extract_daegu_auto_companies()