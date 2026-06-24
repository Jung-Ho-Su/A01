item = 0
zzak = 0
hole = 0

for item in range(1, 101, 1):
    if item % 2 == 0:
        zzak += item
    else:
        hole += item

print(zzak)
print(hole)
