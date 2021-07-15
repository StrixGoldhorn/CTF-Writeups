# bot not not bot

Web<br/>
185 solves, 322 pts<br/>

### Description
Ain't Much, But It's Honest Work!!! https://bot-not-not-bot.vishwactf.com/

<br/><br/><br/>

### Solution
From the index, we visit page1.html<br/>
It says “Useless Page -1”<br/>
The following pages seems to be the same, until page8.html<br/>
It displays “v Useful Page 0”<br/>
Then, we write a script to go through all 500 pages and extract out the first and last displayed character<br/>
We then realise that the last character denotes the index of the first character in the string of the flag<br/>
````Python
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
````
[Script](Assets/notbot.py)
<br/>
> vishwaCTF{r0bot_15_t00_0P}