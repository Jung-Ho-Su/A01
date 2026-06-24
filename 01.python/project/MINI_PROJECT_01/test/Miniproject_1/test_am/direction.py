import pandas as pd
import os


def filter_to_chungnam():
    # 1. 파일 불러오기
    input_file = '전라북도_출발_영업소간_교통량.csv'

    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return

    try:
        df = pd.read_csv(input_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(input_file, encoding='cp949')

    # 2. 전처리: 컬럼명 및 데이터 공백 제거
    df.columns = [col.strip().replace('"', '') for col in df.columns]
    df['도착영업소명'] = df['도착영업소명'].astype(str).str.strip()

    # 3. 충청남도(충남) 소재 주요 영업소 리스트
    # 데이터셋 내에 존재하는 충남 지역 톨게이트들입니다.
    chungnam_offices = [
        '천안', '북천안', '남천안', '서천안', '목천', '풍세상', '풍세하', '남풍세', '독립기념관',
        '아산', '아산현충사', '온양', '공주', '남공주', '서공주', '유구', '마곡사', '정안', '탄천',
        '논산', '서논산', '남논산상', '남논산하', '연무', '양촌', '계룡',
        '금산', '추부', '부여', '서부여', '서천', '동서천', '춘장대', '무창포', '대천',
        '서산', '해미', '당진', '송악', '면천', '고덕', '예산수덕사', '신양', '홍성', '광천', '칠갑산'
    ]

    # 💡 (참고) 만약 세종/대전 지역까지 포함하고 싶다면 아래 리스트를 위 리스트에 추가하세요.
    # extra_offices = ['서세종', '남세종', '대전', '북대전', '서대전', '남대전', '안영', '유성', '신탄진', '판암']

    # 4. 🎯 충남 지역 도착 데이터만 필터링
    cn_dest_df = df[df['도착영업소명'].isin(chungnam_offices)].copy()

    if cn_dest_df.empty:
        print("❌ 충남 지역으로 도착하는 데이터를 찾지 못했습니다. 리스트를 확인해 보세요.")
        return

    # 5. 결과 저장
    output_filename = '전북출발_충남도착_교통량.csv'
    cn_dest_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("=" * 60)
    print(f"✅ 필터링 완료! 충남 지역 {len(chungnam_offices)}개 영업소로 향하는 데이터를 추출했습니다.")
    print(f"📊 추출된 데이터 수: {len(cn_dest_df):,}건")
    print(f"💾 파일이 저장되었습니다: {output_filename}")
    print("=" * 60)

    # 상위 5개 데이터 미리보기
    print("\n[추출 데이터 미리보기]")
    print(cn_dest_df[['출발영업소명', '도착영업소명', '도착지방향총교통량']].head())


if __name__ == "__main__":
    filter_to_chungnam()