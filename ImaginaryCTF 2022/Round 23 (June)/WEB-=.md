# Web/=
### Eth007

## Description
I don't know PHP

http://eth007.me/lol.php

## Solution
Upon visiting the site, we are greeted with the following code:
```php
<?php
    include('flag.php');
    if ($_GET['a'] !== $_GET['b'] && $_GET['a'] == $_GET['b']) {
        echo $FLAG;
    }
    else {
    highlight_file(__FILE__);
    }
?>
```

This is the typical `==` vs `===` comparison trick

Hence, we set `a` to `0e1` and `b` to `0e2`, so `a` and `b` are both evaluated as `0`

> ictf{d0nt_use_loose_comparisons_1b19d312}