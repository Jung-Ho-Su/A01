import random
lst = []

while True:
    random.randint(1,45)
    su = lst.append(random.randint(1,45))
    if su in lst:
        pass
    if len(lst) > 6:
        print("LOTTO :", lst)
        break