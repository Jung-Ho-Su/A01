import pandas as pd
import folium
from folium.plugins import MarkerCluster
import requests
import time

# 1. 네이버 API 키 설정 (본인의 키로 수정하세요)
CLIENT_ID = "tRxyx2FZijBtjwOIGPgG"
CLIENT_SECRET = "7um7OvF2bL"


# 2. 주소를 좌표로 변환하는 함수 (네이버 Geocoding API)
def get_coords_naver(address):
    url = f"https://openapi.naver.com/v1/map-geocode/search?query={address}"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }
    try:
        response = requests.get(url, headers=headers).json()
        if 'addresses' in response and len(response['addresses']) > 0:
            # 위도(y), 경도(x) 반환
            return float(response['addresses'][0]['y']), float(response['addresses'][0]['x'])
    except Exception as e:
        return None, None
    return None, None


# 3. 데이터 불러오기
file_path = '전국_철강산업_공장현황.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')

# 4. 전체 데이터 좌표 변환
# 주의: 데이터가 많으면 수십 분이 소요될 수 있습니다.
# 테스트를 원하시면 df = df.head(100)을 먼저 실행해 보세요.
print(f"총 {len(df)}건의 데이터를 변환하기 시작합니다...")

lats, lons = [], []
for i, addr in enumerate(df['공장주소']):
    lat, lon = get_coords_naver(addr)
    lats.append(lat)
    lons.append(lon)

    # 진행 상황 출력 (100건마다)
    if (i + 1) % 100 == 0:
        print(f"진행 중... ({i + 1}/{len(df)})")

df['lat'] = lats
df['lon'] = lons

# 좌표 변환에 성공한 데이터만 추출
df_final = df.dropna(subset=['lat', 'lon'])

# 5. 버블맵 시각화
print("지도를 생성하고 있습니다...")
m = folium.Map(location=[36.5, 127.5], zoom_start=7, tiles='cartodbpositron')

# 마커 클러스터 추가 (데이터가 많으므로 필수)
marker_cluster = MarkerCluster().add_to(m)

for i, row in df_final.iterrows():
    # 종업원 수 기반 버블 크기 설정 (값이 너무 크면 루트 처리)
    emp_count = row['종업원합계'] if pd.notnull(row['종업원합계']) else 5
    radius = (emp_count ** 0.5) * 1.5  # 크기 조정 계수

    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=radius if radius > 2 else 2,
        color='#e74c3c',  # 테두리: 빨강
        fill=True,
        fill_color='#c0392b',  # 채우기: 진한 빨강
        fill_opacity=0.5,
        popup=folium.Popup(f"<b>{row['회사명']}</b><br>생산품: {row['생산품']}<br>종업원: {row['종업원합계']}명", max_width=300)
    ).add_to(marker_cluster)

# 6. 결과 저장
m.save('전국_철강산업_전체_버블맵.html')
print(f"성공적으로 {len(df_final)}개의 공장을 지도에 표시했습니다.")
print("'전국_철강산업_전체_버블맵.html' 파일을 웹 브라우저로 열어보세요.")