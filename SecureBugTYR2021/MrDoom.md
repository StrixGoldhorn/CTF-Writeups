# MrDoom

Web<br/>
Easy, 50 pts<br/>

### Description
[Challenge Link](http://ec2-18-184-207-28.eu-central-1.compute.amazonaws.com/doom/)



### Solution
Viewing the source code gives shows three important chunks of code

First, a hint in the HTML code
````HTML
<!--------------------------------------------
        letter1 : alert('flag1')
        letter2 : alert('flag2')
    ---------------------------------------------->
````
We need to use `alert('flag1')` and `alert('flag2')` to get the 2 halves of the flag

<br/>
Next, a Javascript function required to use, to acquire the first half of the flag

````Javascript
function message1(s) {
	// try "data#data"
	var slice = s.split(/#/);

	if(!(/^[a-zA-Z\[\]']*$/.test(slice[0]))) {
		return document.write('Invalid callback');
	} else {
		var obj = {
			'userdata': slice[1]
		};
		var json = '(' + JSON.stringify(obj).replace(/</g, '\\u003c') + ')';
		return document.getElementById('demo').innerHTML += "<script>" + slice[0] + json;
	}
}
console.log(message1(data));

````

message1() splits the input string, and checks the first half for invalid characters<br/>
It then makes an object with the second half of the key, and we can easily break out of it by using a semicolon<br/>
Doing so allows us to insert our own code into it (ie alert('flag1'))<br/>
We can also then comment out the later section of the code using double backslash<br/>
So, altogether, the input will be `'#';alert('flag1')//`<br/><br/>
We get the first half of the flag 
>FLAG{th!5_!5_my_l0ng_

<br/><br/><br/>
And another Javascript function that needs to be used to acquire the second half of the flag

````Javascript
function message2(s) {
	// try "data#data"
	var d = s.split(/#/);
	var a = document.createElement('div');
	a.appendChild(document['create' + d[0]].apply(document, d.slice(1)));
	return document.getElementById('demo').innerHTML += a.innerHTML;
}
console.log(message2(data));
````
message2() takes the first half of the input and appends it to a document.create_____ function<br/>
We try createElement(), but the only thing it created was an error<br/>
A bit of googling finds us createComment(), which works<br/>
Add in a a script that runs alert(‘flag2’) and you get the second half of the flag<br/>
So, altogether, the input will be `Comment#><script>alert('flag2')</script>`<br/><br/>
We get the second half of the flag
>Fl4g_F0r_5w33t_D0M!!}
<br/>
Note: this was *NOT* the intended solution, which was to use an SVG to run the script, ie `<svg onload=alert('flag2')`

<br/><br/><br/>
Combine the two halves to get the full flag
>FLAG{th!5_!5_my_l0ng_Fl4g_F0r_5w33t_D0M!!}
