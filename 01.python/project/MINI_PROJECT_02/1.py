

import pandas as pd
import numpy as np
import os

# 1. 파일 경로 설정
file_path = 'korea_administrative_division_latitude_longitude.csv'

# 2. 데이터 로드 (csv가 아니라 실제로는 엑셀 형식이므로 read_excel 사용)
try:
    # 파일이 엑셀 형식이므로 engine='openpyxl'을 명시하거나 read_excel을 사용합니다.
    df = pd.read_excel(file_path)
    print("✅ 엑셀 형식으로 파일을 성공적으로 불러왔습니다.")
except Exception as e:
    print(f"❌ 파일 읽기 실패: {e}")
    print("파일이 실제 CSV인지 엑셀인지 확인이 필요합니다.")
    # 만약 진짜 CSV라면 아래 주석을 해제하고 사용하세요.
    # df = pd.read_csv(file_path, encoding='cp949')

if 'df' in locals():
    # 3. 원자력 발전소 좌표 설정
    plants = {
        'Wolseong': (35.74, 129.18),
        'Kori_Saeul': (35.3, 129.2),
        'Hanul': (36.8, 130.2),
        'Hanbit': (35.415, 126.4239)
    }

    def haversine(lat1, lon1, lat2, lon2):
        """두 지점 사이의 거리(km) 계산 함수"""
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return c * 6371

    # 4. 거리 계산 및 컬럼 추가
    # 컬럼명(latitude, longitude)이 엑셀 시트 내의 정확한 이름인지 확인하세요.
    for name, coords in plants.items():
        p_lat, p_lon = coords
        df[f'dist_{name}_km'] = df.apply(
            lambda row: haversine(row['latitude'], row['longitude'], p_lat, p_lon), axis=1
        )

    # 5. 결과 저장
    output_name = 'location_with_distances.csv'
    df.to_csv(output_name, index=False, encoding='utf-8-sig')
    print(f"✅ 계산 완료! '{output_name}' 파일이 생성되었습니다.")
    print(df.head())