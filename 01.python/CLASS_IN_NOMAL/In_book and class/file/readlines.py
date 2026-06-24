with open('hello.txt', 'r', encoding='utf8') as file:
    lines = file.readlines() # -s 는 리스트 형식으로 파일이 나온다.
    print(lines)