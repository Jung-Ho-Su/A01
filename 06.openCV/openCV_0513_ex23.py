# 도형 그리기 (Drawing)
import cv2
import numpy as np

src = np.zeros((768, 1366, 3), dtype=np.uint8)

src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3,
               cv2.LINE_AA) # cv2.LINE_AA : 끝부분을 둥글게 하겠다는 의미!
src = cv2.rectangle(src,(500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8) # cv2.LINE_8 : 각도
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2) # 호 그리기

pts1 = np.array([[100, 500], [300, 500], [200, 600]]) # 3개의 좌표를 찍어서 연결하는 것
pts2 = np.array([[600, 500], [800, 500], [700, 600]]) # 이것도 마찬가지로 연결하는 것
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2) # 색으로 채우는 기능이 없음 ㅠㅠ 그냥 도형만 그려짐
src = cv2.fillPoly(src, [pts2], (0, 0, 255), cv2.LINE_AA) # 색으로 채우는 기능

src = cv2.putText(src, "Ryan", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, # 텍스트 출력하는 부분 , 글꼴을 테스트 해보쟝
                  (255, 255, 255), 3)

src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()