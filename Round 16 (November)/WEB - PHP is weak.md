# PHP is weak?

## Description
Php is weak for cookie defending I think !!!

https://php-is-weak.ictf.iciaran.com/

## Solution
1. Viewing the source code, we see a comment that says `frpergnybat.gkg`
2. Using ROT13, we get `secretalong.txt`
3. Visiting [/secretalong.txt](https://php-is-weak.ictf.iciaran.com/secretalong.txt), we see this:
```
Don't tell anyone about that!! Okay??
admin_gmail: "admin@gmail.com"
admin_password: "secret_password_12345789!!!"
# Btw "Remember me" button is important for me because i forgot my creds always.
```
4. Logging in using the given credentials and checking "Remember me", we are logged in
5. Checking the cookies, there is a cookie called `flag` with value `aWN0ZntjMG9va2llX3NUZWFsaW5nX2lzX05pY2UhISFfMTU4N30%3D`
6. Decoding as URL then decoding as Base64, we get the flag `ictf{c0ookie_sTealing_is_Nice!!!_1587}`

> ictf{c0ookie_sTealing_is_Nice!!!_1587}