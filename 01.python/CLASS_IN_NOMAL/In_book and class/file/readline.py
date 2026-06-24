with open('hello.txt', 'r', encoding='utf8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))