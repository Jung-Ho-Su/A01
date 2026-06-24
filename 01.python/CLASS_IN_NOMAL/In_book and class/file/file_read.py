file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()
# hello.txt.파일을 읽기 모드(r)로 열기, read는 해당파일의 내용을 첫번째부터 마지막까지 모두 읽음
# 모두 읽은 파일의 내용을 변수 s에 모두 반환시킴 / 한꺼번에 읽어서 모두 반환 / 이때 변수는 문자열 형태로 반환시킴
#파일에서 문자열 열기 readline()

#with 문은 파일을 자동으로 닫아주지만 해당 with문 내에서 사용해야한다.