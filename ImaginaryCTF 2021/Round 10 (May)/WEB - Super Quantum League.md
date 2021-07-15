# Super Quantum League

97 pts<br/>

### Description
The admin user looks interesting. Find admin's password.

### Attachments
http://superquantumleague.imaginary.ml/ https://imaginary.ml/r/8863-superquantumleague.py

### Author
Eth007

<br/><br/><br/>

### Solution
From the [provided source code](Assets/superquantumleague.py), we can see that it is a blind sqli challenge<br/>
1. First, we need to find the characters present in the password/flag
2. For this, we use the query `SELECT * FROM users WHERE username='admin' AND password LIKE '%{char}%' -- `
3. Using the characters, we brute force each character of the password, starting from the first.
4. For this, we use the query `SELECT * FROM users WHERE username='admin' AND password LIKE '{known_password}%' -- `
<br/>

[Solve script](Assets/blindsqli.py)

<br/>
> ictf{bl1nd_1nj3ct1on_ftw_5a7566bc}
