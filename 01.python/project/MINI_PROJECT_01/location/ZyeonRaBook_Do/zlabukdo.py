import pandas as pd
import os


def extract_jeonbuk_auto_companies():
    # 1. 처리할 전북특별자치도 6개 파일 목록
    files = [
        "전북특별자치도 군산시_제조업공장현황_20250623.csv",
        "전북특별자치도 김제시_제조업공장현황_20250702.csv",
        "전북특별자치도 부안군_제조업 공장 현황_20250730.csv",
        "전북특별자치도 전주시_제조업_20260223.csv",
        "전북특별자치도_공장현황_20170421.csv",
        "전북특별자치도_제조업체 현황_20211231.csv"
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

        # 열 이름에 보이지 않는 공백이 있을 경우를 대비해 양옆 공백 제거
        df.columns = df.columns.str.strip()

        # 3. 데이터 필터링 (모든 컬럼을 텍스트로 변환 후 키워드 검색)
        mask = df.astype(str).apply(lambda col: col.str.contains(search_pattern, na=False, case=False)).any(axis=1)
        filtered_df = df[mask].copy()

        if not filtered_df.empty:
            # 4. 전북 지자체별로 제각각인 컬럼명을 공통 컬럼명으로 통일

            # [회사명] 통일 ('회사명', '사업체명', '상호명')
            company_cols = ['회사명', '사업체명', '상호명', '업체명']
            filtered_df['통합_회사명'] = ""
            for col in company_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_회사명'] = filtered_df['통합_회사명'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [업종명] 통일 ('업종명', '업종', '업종구분')
            industry_cols = ['업종명', '업종', '업종구분']
            filtered_df['통합_업종명'] = ""
            for col in industry_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_업종명'] = filtered_df['통합_업종명'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [생산품] 통일 ('생산품', '주생산품', '생산품목')
            prod_cols = ['생산품', '주생산품', '생산품목']
            filtered_df['통합_생산품'] = ""
            for col in prod_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_생산품'] = filtered_df['통합_생산품'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [주소] 통일 ('공장대표주소', '도로명주소', '주소', '공장대표주소(도로명)')
            addr_cols = ['공장대표주소', '공장대표주소(도로명)', '도로명주소', '주소', '소재지주소', '소재지']
            filtered_df['통합_주소'] = ""
            for col in addr_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_주소'] = filtered_df['통합_주소'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [연락처] 통일 ('전화번호', '연락처')
            tel_cols = ['전화번호', '연락처']
            filtered_df['통합_연락처'] = ""
            for col in tel_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_연락처'] = filtered_df['통합_연락처'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [출처파일] 기록
            filtered_df['출처파일'] = file

            # 5. 통일된 핵심 컬럼만 잘라내기
            final_cols = ['통합_회사명', '통합_업종명', '통합_생산품', '통합_주소', '통합_연락처', '출처파일']

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

            # 6. 의미 없는 데이터 정리 (회사명이 비어있거나 숫자만 있는 경우 필터링)
            clean_df = clean_df[clean_df['회사명'].astype(str).str.strip() != ""]
            clean_df = clean_df[~clean_df['회사명'].astype(str).str.match(r'^\d+$')]

            if not clean_df.empty:
                extracted_dataframes.append(clean_df)
                print(f"✔️ [{file}] 추출 완료: {len(clean_df)}건의 관련 회사 발견")
            else:
                print(f"➖ [{file}] 자동차 관련 데이터 없음 (또는 통계용 파일)")

    # 7. 최종 데이터를 병합하여 CSV 파일로 저장
    if extracted_dataframes:
        # 데이터프레임 병합 및 빈 값(NaN) 처리
        final_result = pd.concat(extracted_dataframes, ignore_index=True).fillna("")

        # 중복 데이터 제거 (회사명과 주소가 동일한 데이터가 중복으로 존재할 경우 첫 번째 항목만 남김)
        final_result = final_result.drop_duplicates(subset=['회사명', '주소'], keep='first')

        # 저장할 파일명 지정
        output_file = "전북특별자치도_자동차산업_관련_회사목록_통합본.csv"

        # 엑셀에서 바로 열어도 한글이 깨지지 않도록 utf-8-sig 인코딩으로 저장
        final_result.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"\n✅ 작업 완료! 중복 제거 후 총 {len(final_result)}개의 데이터가 병합되어 저장되었습니다.")
        print(f"👉 파일명: {output_file} (엑셀에서 더블클릭하여 바로 확인 가능합니다)")
    else:
        print("\n자동차 산업 관련 회사를 찾을 수 없습니다.")


if __name__ == "__main__":
    extract_jeonbuk_auto_companies()