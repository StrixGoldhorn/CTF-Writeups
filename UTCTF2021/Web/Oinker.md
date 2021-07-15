# Oinker

Web<br/>
452 solves, 100 pts<br/>

### Description
I found this cool more private alternative to twitter.<br/>
http://web2.utctf.live:5320/<br/>
-- a1c3<br/>

<br/><br/><br/>

### Solution
We submit random letters, and it directs us to a new link http://web2.utctf.live:5320/oink/51<br/>
We go back and submit the same letters, and it still directs us to a new link http://web2.utctf.live:5320/oink/52 <br/>
Hence, we go to the first one, http://web2.utctf.live:5320/oink/1 and it shows “testing oink”<br/>
We then visit the second, http://web2.utctf.live:5320/oink/2 and it gives us the flag<br/>
<br/>
> utflag{traversal_bad_dude}