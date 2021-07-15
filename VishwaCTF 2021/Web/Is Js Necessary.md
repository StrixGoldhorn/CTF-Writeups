# Is Js Necessary

Web<br/>
152 solves, 382 pts<br/>

### Description
https://isjsnecessary.vishwactf.com

<br/><br/><br/>

### Solution
We visit the site and note that it redirects us to Google<br/>
Thus, we pause the loading of the site by going to the developer console, hit ctrl+shift+p, and search for disable javascript<br/>
We then visit the site, and view source code and find the javascript code<br/>
````Js
window.setTimeout(function () {window.location.href = "https://www.google.co.in";}, 200);
    const studentsOfcyberCellare = "awesome";
    if(studentsOfcyberCellare == "awesome")
    document.getElementById("therealdeal").style.visibility = "hidden";
````
First, we remove the redirect<br/>
Then, we change the visibility from hidden to visible<br/>
We then submit any number, to get an alert with the flag<br/>
<br/>
> vishwaCTF{2ava5cr1pt_can_be_Dis@bleD}