# dct = {}
# dct['id'] = 'hong'
# dct['pw'] = '1234'
# print(dct)
#
# dct['email'] = 'hong@gmail.com'
# print(dct)
# dct['id'] = 'lee'
# print(dct)
#
# del dct['email']
# print(dct)

dct = {}
dct['id'] = 'hong'
dct['pw'] = '1234'
dct['email'] = 'hong@gmail.com'
print(dct)
print(dct.keys())
print(dct.values())
print(dct.items())

res = dct.get('id') # dct['id']
print(res)
dct.clear()
print(dct)