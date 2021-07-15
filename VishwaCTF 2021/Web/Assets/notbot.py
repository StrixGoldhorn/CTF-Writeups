import requests
import urllib.request

urlbase = 'https://bot-not-not-bot.vishwactf.com/page'
x = ""
y = ""
z = []

for i in range(0,50):
    z.append("~")

for i in range(1,501):
    url = urlbase+str(i)+".html"
    r = requests.get(url)
    s = str(r.text.splitlines())
    if "Useful" in s:
        a = s.index("<h1>")
        b = s.index("</h1>")
        c = s.index("<br>")
        d = s.index("</p>")
        print(i, s, s[a+4:b], s[c+4:d])
        x = s[a+4:b]
        y = s[c+4:d]
        z[int(y)]= x
        

print("DONE:")
z = ''.join(z)
print(z)

