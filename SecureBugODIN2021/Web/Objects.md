# Objects

Web<br/>
Hard, 200 pts<br/>

### Description
I love mango and i love db too.<br/>
https://ch8.sbug.se <br/>

<br/><br/><br/>

### Solution
Visiting `/robots.txt`, we find 2 interesting locations, `/l0g.hacker` and `/index.php~`<br/>
l0g.hacker contains: <br/>

````
Mon May 27 2019 10:01:40 GMT+0800 (UTC)   Start service
Mon May 27 2019 13:24:45 GMT+0800 (UTC)   Start database
Sat May 20 2019 22:53:32 GMT+0800 (UTC)   Start Updated
Fri May 30 2019 12:46:59 GMT+0800 (UTC)   Flag Added Here
````

index.php contains: <br/>
````PHP
<?php
if ( $_GET['flag_id'] == $flagid ){ echo $flag; }
 
/*
u need to get the flag ID, and use this ids ;)
IDs:
5ceb45045c1fa2a0df9f3da7
5ceb749d5c1fa2a0df9f3da8
5ce2bf6c5c1fa2a0df9f3da9
i love mongo remember that.
*/
````

We find that the IDs are mongodb IDs and the 8 characters correspods to the date<br/>
We also realise that the last character is increasing<br/>
Hence, we realise that the ID for the log when flag was added is `5cef60435c1fa2a0df9f3daa`<br/>

<br/>
> FLAG{0bj3ct_Id$_!s_w0Nd3rFul}