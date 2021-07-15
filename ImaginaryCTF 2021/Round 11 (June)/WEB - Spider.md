# Run-ELF

### Description
Got some glue?

Note: There's a rate limiter of 3 requests/second

### Attachments
https://spider.031337.xyz

### Author
Robin_Jadoul

### Points
75

<br/><br/><br/>

### Solution
Using BurpSuite, we visit the website to find a page that says `Hello 0`<br/>
Digging deeper, we find the requests headers are
```
'Content-Length': '8'
'Content-Type': 'text/html; charset=utf-8'
'Date': 'Wed, 02 Jun 2021 16:31:02 GMT'
'Server': 'Caddy, Werkzeug/2.0.1 Python/3.8.5'
'X-Flag': 'i'
```
Interesting, a header `X-Flag` set to `i`, which is (not) coincidentally, the first character of the flag format, `ictf{...}`<br/>
We originally used Burp to go through the characters until we got the flag, but after submitting, we created a [short python script](Assets/Spider.py) to do it for us<br/>

```Python
import requests

url = 'https://spider.031337.xyz/'
flag = ''

for i in range(25):
    r = requests.get(url+str(i))
    flag += r.headers['X-Flag']

print(flag)
```

<br/>
> ictf{f0ll0w_th3_numb3rs}