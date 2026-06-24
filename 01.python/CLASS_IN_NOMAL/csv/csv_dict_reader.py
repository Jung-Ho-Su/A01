import csv

f = open("data2.csv", "r")
reader = csv.DictReader(f)
# print(list(reader))

for row in reader:
    print(row)

f.close()