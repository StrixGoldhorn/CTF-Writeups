import requests

url = 'https://spider.031337.xyz/'
flag = ''

for i in range(25):
    r = requests.get(url+str(i))
    flag += r.headers['X-Flag']

print(f'flag')