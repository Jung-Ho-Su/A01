import pandas as pd
import requests
import time
from tqdm import tqdm

# ==========================================
# 🔑 카카오 REST API 키 입력 (필수)
# 카카오 디벨로퍼스(developers.kakao.com)에서 무료 발급
# ==========================================
KAKAO_API_KEY = "a056117429339d0aa150b60ac6703bd4"


def get_lat_lng(address, headers):
    """카카오 API를 이용해 주소를 위도, 경도로 변환"""
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={address}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result['documents']:
                match = result['documents'][0]
                return float(match['y']), float(match['x'])  # y: 위도, x: 경도
    except Exception as e:
        pass
    return None, None


def process_geocoding():
    file_path = '한국산업단지공단_전국등록공장현황_등록공장현황자료_20241231.csv'

    print("1. 데이터를 불러오는 중...")
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"총 데이터 건수: {len(df):,}건")

    # 공장주소 컬럼 문자열 처리
    df['공장주소'] = df['공장주소'].astype(str).str.strip()

    # API 호출 최적화: 고유한 주소만 추출해서 먼저 변환 (속도 대폭 향상)
    unique_addresses = df['공장주소'].unique()
    print(f"중복 제외 고유 주소 건수: {len(unique_addresses):,}건")

    address_cache = {}  # 주소: (위도, 경도) 저장용 딕셔너리
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}

    print("\n2. 카카오 API 위경도 변환 시작...")
    for address in tqdm(unique_addresses, desc="Geocoding Progress"):
        if address and address != 'nan':
            lat, lng = get_lat_lng(address, headers)
            address_cache[address] = (lat, lng)
            time.sleep(0.02)  # API 서버 과부하 방지 (초당 50건)
        else:
            address_cache[address] = (None, None)

    print("\n3. 변환된 좌표를 원본 데이터에 매핑하는 중...")
    # 캐싱된 딕셔너리를 활용해 전체 데이터프레임에 빠르게 매핑
    df['위도'] = df['공장주소'].map(lambda x: address_cache.get(x, (None, None))[0])
    df['경도'] = df['공장주소'].map(lambda x: address_cache.get(x, (None, None))[1])

    # 실패 건수 확인
    failed_count = df['위도'].isna().sum()
    print(f"✅ 변환 완료! (성공: {len(df) - failed_count:,}건 / 실패(주소불량 등): {failed_count:,}건)")

    # 4. 결과 저장
    output_filename = '전국공장현황_위경도추가완료.csv'
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"\n💾 최종 파일이 '{output_filename}' 이름으로 저장되었습니다!")


if __name__ == "__main__":
    if KAKAO_API_KEY == "여기에_발급받은_REST_API_키를_넣어주세요":
        print("❌ 실행 에러: 코드 상단의 'KAKAO_API_KEY'에 카카오 API 키를 먼저 입력해주세요!")
    else:
        process_geocoding()