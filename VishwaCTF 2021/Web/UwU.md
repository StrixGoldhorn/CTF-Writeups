# UwU

Web<br/>
98 solves, 449 pts<br/>

### Description
when php, anime and robots come together. they make hell of a challenge. https://uwu.vishwactf.com/<br/>

<br/><br/><br/>

### Solution
First, we visit robots.txt<br/>
It is different from other usual robots.txt<br/>
“this time.. there might be a directory called as robots lol”<br/>
We then visit /robots/<br/>
There is a button for us to view source code<br/>
````PHP
<?php
  require("cyberflagster.php");  
  $try; //1
  $function; //5
  if (isset($_GET['showThem'])) {
   
    highlight_file(__FILE__);
   
    die();
  
  }
   $reach;//3
  if (isset($_GET['php_is_hard'])) {
  
    $you_enter = $_GET['php_is_hard'];
  
    $we_enter = 'suzuki_harumiya';
  
    $the_final_one = preg_replace(
    
      "/$we_enter/", '', $you_enter);
  
      if ($the_final_one === $we_enter) {
  
        open_up();
    }
  }
  $to; //2
  $open_up;//4
?>
````
What does preg_replace(“$x”,”$y”,”$z”) do?<br/>
It searches for a $x string inside $z, and if $x is present, replaces $x with $y<br/>
Back to the code:<br/>
At first glance, it may seem impossible, as preg_replace() replaces the very string needed to get the flag<br/>
However, a neat trick is to divide the string needed into 2 parts, and place the same string in the middle<br/>
When it undergoes preg_replace(), it essentially removes the string in the middle, and the result will be the required string<br/>
Hence, we set $php_is_hard to “suzuki_harusuzuki_harumiyamiya”, and we get the flag<br/>

<br/>
> vishwaCTF{well_this_was_a_journey}