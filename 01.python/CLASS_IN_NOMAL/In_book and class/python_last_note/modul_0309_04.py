# os 모듈 : 운영체제에서 제공하는 정보를 제공하거나 운영체제의 기능을 사용할 수 있는 방법을 제공
import os

print(os.name) # 운영 체제의 종류를 알려줌
print(os.getcwd()) # 현재의 경로를 알려줌
print(os.path.join(os.getcwd(), "../../test")) # 현재 경로와 "" 를 연결시켜서 반환시켜줌

os.mkdir(os.path.join(os.getcwd(), "../../test")) # mkdir : 해당 경로를 가지고 디렉토리를 만들어라는 뜻
# 얘는 한번만 실행히켜야함 두번 시키면 에러가 남 # why? : 디렉토리가 이미 있는데 또 만들면 에러가 난다.
# 얘르 나중에 사용하려면 해당 디렉토리나 파일이 있는지 확인하는 작업이 필요함 : os.path.exist

##os.rmidr(os.path.join(os.getcwd(), "test")) # 테스트 폴더 안에 아무것도 없는 상태라면 해당 디렉토리를 삭제할 수 있는 함수
##os.remove(os.path.join(os.getcwd(), "test.py")) # 해당 파일을 삭제 할 때 사용하는 기능이다. 해당 파일을 삭제하는 기능



# ch : 경로를 변경하라는 뜻 // \\ : 백슬래시 문자 그 자체를 한 개 출력하게 된다.
os.chdir("c:\\windows")
print(os.getcwd())
print(os.listdir())



