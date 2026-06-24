import csv
f = open('sangpum_data.txt', 'r', encoding='utf-8')
reader = csv.DictReader(f)

for row in reader:
    print(row)

f.close()