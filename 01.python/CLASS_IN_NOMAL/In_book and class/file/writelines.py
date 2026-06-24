# 한꺼번에 3개의 문자열을 출력하는 형태
lines = ['안녕하세요.\n','파이썬\n','코딩 도장입니다.\n']

with open('test.txt', 'w', encoding="utf-8") as file: #encoding="utf-8" 한글이 깨지지 않고 인코딩 해줌
    file.writelines(lines)