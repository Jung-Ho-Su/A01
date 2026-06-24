#1.1 문자열 바꾸기
a = 'Hello world!'.replace('world', 'python')
print(a)

s = 'hello world!'
s = s.replace('world', 'python')
print(s)

#1.2 문자 바꾸기
table =str.maketrans('aeiou', '12345')
b = 'apple'.translate(table)
print(b)

#1.3 문자열 분리하기
c = 'apple pear grape pineapple orange'.split()
print(c)

d = 'apple, pear, grape, pineapple, orange'.split(',')
print(d)

#1.4 구분자 문자열과 문자열 리스트 연결하기
e = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(e)
f = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(f)

#1.5 소문자를 대문자로 바꾸기
print('python'.upper())

#1.6 대문자를 소문자로 바꾸기
print('PYTHON'.lower())

#1.789 왼쪽 공백 삭제하기
g = "   python   ".lstrip()
print(g)

h = "   python   ".rstrip()
print(h)

i = "   python   ".strip()
print(i)

#1.10
