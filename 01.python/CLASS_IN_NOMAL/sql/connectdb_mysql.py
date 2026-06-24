import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       db = 'tabledb',
                       charset='utf8')
cursor = conn.cursor() # sql문을 실행할 수 있는 명령문을 cursor커서 객체가 정해준다.

sql = 'SELECT * FROM usertbl'
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()

# 연결 객체 생성 >> 커서 객체 생성 >>> sql문 실행 >> 다 끝나면 커서연결 객체도 닫아주는 순서로 실행한다.