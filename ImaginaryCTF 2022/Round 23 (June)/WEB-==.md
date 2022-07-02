# Web/==
### Eth007

## Description
I still don't know php 😭

http://eth007.me/lol2.php

## Solution
Upon visiting the site, we are greeted with the following code:
```php
<?php
    include('flag2.php');
    if ($_GET['a'] && $_GET['b'] && $_GET['a'] != "" && $_GET['b'] != "") {
        if ($_GET['a'] !== $_GET['b'] && "ictf{".$_GET['a']."}" === "ictf{".$_GET['b']."}") {
           echo $FLAG;
        }
    }
    highlight_file(__FILE__);
?>
```

When concaternated, an array will output as `Array`

Hence, we set parameters `a=Array` and `b[]=`, such that `b` is different from `a`, but when concaternated, they will be the same.

> ictf{arr4yyyyyyyyyyyyyyyyyyyy_29d92bf3}