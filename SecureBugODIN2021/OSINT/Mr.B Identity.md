# Mr.B Identity

OSINT<br/>
Easy, 50 pts<br/>

### Description
"A person known as Mr.B claims that he has discovered information about a secret project that affects people all around the world, we couldn't find a way to talk to him yet, but some say he shared his email address on the internet for people to contact him.<br/>
All we know about him besides his alias, is a strange name known to be used by him (THE4llANDP0werfu1MrB).<br/>
Find his email address and submit the flag like below:<br/>
Email: exampleMailTest@test.com, Flag: SBCTF{exampleMailTest}"<br/>

<br/><br/><br/>

### Solution
We google `"THE4llANDP0werfu1MrB"` and find [his reddit account](https://www.reddit.com/user/THE4llANDP0werfu1MrB/)<br/>
We decode a Base 64 string in his description `SGVyZSdzIG15IGVtYWlsIGFkZHJlc3M6IHByaXZhdGVNYWlsT2ZNckJAcHJvdG9ubWFpbC5jb20sIGJ1dCBJIHdpbGwgTk9UIHJlcGx5IGluIGFueSB3YXkgb3IgZm9ybSwgc28gZG9uJ3QgYm90aGVyLg==`<br/>
We get his email `privateMailOfMrB@protonmail.com`<br/>
<br/>
> SBCTF{privateMailOfMrB}