# Sessions

Web<br/>
302 solves, 100 pts<br/>

### Description
Find the flag.<br/>
[http://34.69.61.54:4777](http://34.69.61.54:4777)<br/>
Author: f1rehaz4rd<br/>

<br/><br/><br/>

### Solution
When first visiting the site, it brings us to [/login](http://34.69.61.54:4777/login)<br/>
Inspecting the source code, we see this: `<!--#remove comment later: login iroh:iroh-->`<br/>
We thus use 'iroh' for both the username and password<br/>
Next, we realise that a new cookie has been added: `UlN7MG5seV9PbmVfczNzc2lvbl90b2szbn0=`<br/>
Decoding it from base 64 gives us the flag<br/>
<br/>
> RS{0nly_One_s3ssion_tok3n}