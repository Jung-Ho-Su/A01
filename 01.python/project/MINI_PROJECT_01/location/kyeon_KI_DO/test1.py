import pandas as pd
import os


def extract_gyeonggi_auto_companies():
    # 1. 처리할 경기도 10개 파일 목록
    files = [
        "경기도_고양시_공장등록 현황_20251210.csv",
        "경기도 과천시_공장 현황_20260114.csv",
        "경기도 광명시_공장등록현황_20251208.csv",
        "경기도 광주시_공장등록 현황_20260130.csv",
        "경기도 군포시_공장등록 현황_20250915.csv",
        "경기도 부천시_공장등록현황_20251118.csv",
        "경기도 성남시_업체_및_공장등록_현황_20260309.csv",
        "경기도 수원시_제조업현황_20250214.csv",
        "경기도 시흥시_공장등록현황_20250618.csv",
        "경기도 여주시_공장등록_20251229.csv"
    ]

    # 검색 키워드
    keywords = ['자동차', '차량', '부품', '모터스', '오토']
    search_pattern = '|'.join(keywords)

    extracted_dataframes = []

    for file in files:
        if not os.path.exists(file):
            print(f"경고: [{file}] 파일을 찾을 수 없습니다.")
            continue

        # 2. 파일 불러오기 (인코딩 자동 처리)
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='cp949')

        # 3. 데이터 필터링 (키워드 포함 행 찾기)
        mask = df.astype(str).apply(lambda col: col.str.contains(search_pattern, na=False, case=False)).any(axis=1)
        filtered_df = df[mask].copy()

        if not filtered_df.empty:
            # 4. 지자체별로 제각각인 컬럼명을 공통 컬럼명으로 통일

            # [회사명] 통일
            company_col = '회사명' if '회사명' in filtered_df.columns else ('업체명' if '업체명' in filtered_df.columns else None)
            filtered_df['통합_회사명'] = filtered_df[company_col] if company_col else ""

            # [업종명] 통일
            filtered_df['통합_업종명'] = filtered_df.get('업종명', "")

            # [생산품] 통일
            prod_col = next((col for col in ['생산품', '생산품정보', '생산품목'] if col in filtered_df.columns), None)
            filtered_df['통합_생산품'] = filtered_df[prod_col] if prod_col else ""

            # [주소] 통일 (우선순위를 두어 존재하는 주소 컬럼을 가져옴)
            addr_cols = ['공장대표주소(도로명)', '소재지도로명주소', '공장소재지주소', '도로명주소', '주소', '공장대표주소', '소재지지번주소', '지번주소']
            filtered_df['통합_주소'] = ""
            for col in addr_cols:
                if col in filtered_df.columns:
                    filtered_df['통합_주소'] = filtered_df['통합_주소'].replace("", pd.NA).fillna(filtered_df[col]).fillna("")

            # [연락처] 통일
            filtered_df['통합_연락처'] = filtered_df.get('전화번호', "")

            # [출처파일] 기록
            filtered_df['출처파일'] = file

            # 5. 통일된 핵심 컬럼만 잘라내기
            final_cols = ['통합_회사명', '통합_업종명', '통합_생산품', '통합_주소', '통합_연락처', '출처파일']
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
        # 데이터프레임들을 하나로 합치고 빈 값(NaN)을 빈 문자열로 깔끔하게 처리
        final_result = pd.concat(extracted_dataframes, ignore_index=True).fillna("")

        # 저장할 파일명
        output_file = "경기도_자동차산업_관련_회사목록_통합본.csv"

        # 엑셀에서 바로 열어도 한글이 깨지지 않도록 utf-8-sig 사용 (openpyxl 불필요)
        final_result.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"\n✅ 작업 완료! 총 {len(final_result)}개의 데이터가 병합되어 저장되었습니다.")
        print(f"👉 파일명: {output_file} (엑셀에서 더블클릭하여 바로 확인 가능합니다)")
    else:
        print("\n자동차 산업 관련 회사를 찾을 수 없습니다.")


if __name__ == "__main__":
    extract_gyeonggi_auto_companies()
