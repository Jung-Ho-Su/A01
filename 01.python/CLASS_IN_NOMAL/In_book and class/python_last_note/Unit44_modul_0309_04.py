import urllib.request as r

response = r.urlopen('https://www.google.co.kr')
print(response.status)
print(response)
print(response.read())
