import requests
import urllib.request
import time

urlbase = 'http://167.71.246.232:8080/rabbit_hole.php?page='
combi = []
s = ['','cE4g5bWZtYCuovEgYSO1']

for i in range(0,1582):
    time.sleep(0.01)
    url = str(urlbase+str(s[1]).strip())
    print(i,":",url)
    r = requests.get(url)
    s = r.text.splitlines()
    ts = s[0][1:-1]
    t=list(ts.split(", "))
    t1=t[1]
    t1=t1[1:-1]
    t[1]=t1
    combi.append(t)

print("DONE: ", combi)

