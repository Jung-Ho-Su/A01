# 파일을 출력할 때 csv 형식으로 출력하는 방법이 아래의 예제이다.
#

import csv

f = open('output.csv', 'w', encoding='utf-8', newline='')
#quotechar='"' : 데이터를 묶을 문자 지정
# csv.QUOTE_ALL : 모두 사용하겠다는 의미
wr = csv.writer(f, delimiter=",", quotechar='*', quoting=csv.QUOTE_ALL)
# delimiter="," 구분자
#

wr.writerow([1, "김정수", False])
wr.writerow([2, "박상미", True])
# writerow : 행 단위를 출력할 때 쓰는 기능
# 리스트 형태로 출력하는게 csv 파일을 여는데 일반적이다..
f.close()
