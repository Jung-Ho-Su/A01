import csv

fileldnames = ['code', 'name', 'price', 'amount']
data = [
    {'code' : '1', 'name' : 'apple', 'price' : '5000', 'amount' : '5'},
    {'code' : '2', 'name' : 'pencil', 'price' : '500', 'amount' : '42'},
    {'code' : '3', 'name' : 'pineapple', 'price' : '8000', 'amount' : '5'},
    {'code' : '4', 'name' : 'pen', 'price' : '1500', 'amount' : '10'}
]

f = open('sangpum_data.txt', 'w')
writer = csv.DictWriter(f,fieldnames=fileldnames)

writer.writeheader()
writer.writerows(data)

# for row in data:
#       writer.writerow(row)
# 한 줄 씩 출력하기 위해서 사용하는 것이다.
# for 문으로 한 행 씩 출력한다.

f.close()
