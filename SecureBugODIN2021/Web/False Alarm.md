# False Alarm

Web<br/>
Easy, 50 pts<br/>

### Description
try to make a dummy alert<br/>
https://ch6.sbug.se <br/>

<br/><br/><br/>

### Solution
Inspecting the source code, we find an interesting piece of Javascript<br/>
```JS
function loadObj(){
 var cc=eval('('+unescape(aacc)+')');
 document.getElementById('msg').textContent=cc.message;
}

if(window.location.hash.indexOf('mass')==-1)
  var aacc="({\"message\":\"Hello User!\"})";
else
  var aacc=location.hash.substr(window.location.hash.indexOf('mass=')+5);


var tmp =location.hash;
$.ajax({
type: "POST",
url: "Tc5IQib027qvyjSMfHjOMaLk.php",
data: {"tmp":tmp},
success: function(data,status){
    eval(data)
    }
}); 
```
We note that the POST-ed string will be `location.hash`<br/>
We realise that the string we send must start with "mass="<br/>
Since we must send an alert, we make sure that aacc = alert(1)<br/>
Hence, in the POST request, we set tmp as `"mass=alert(1)"`<br/>
<br/>
> FLAG{DOMDOM-XSS-1337}