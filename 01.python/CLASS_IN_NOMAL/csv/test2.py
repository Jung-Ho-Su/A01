import csv

f = open('output.csv', 'r', encoding='utf-8', newline='')
reader = list(csv.DictReader(f))
print(reader)
for row in reader:
    print(row)

f.close()