# Speedrun 3

Web<br/>


### Description
[http://challenges.ctfd.io:30043/](http://challenges.ctfd.io:30043/)

<br/><br/><br/>

### Solution

#### Discovery
First, we enter the site and randomly fill in the input<br/>
We then refresh it and see `{"admin":false,"name":"asd"}`<br/>
We also note that a cookie, named `authtoken` was created, with the value `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ZmFsc2UsIm5hbWUiOiJhc2QifQ.i9II9riAxP5OSQrVDrRX2dOnNaJI_K4Vk9FED-ADuVs`<br/>
We play around with the cookie by deleting half of it, and was greeted with an error<br/>
`Fatal error: Uncaught UnexpectedValueException: Wrong number of segments in /var/www/html/index.php:84 Stack trace: #0 /var/www/html/index.php(531): Firebase\JWT\JWT::decode('eyJ0eXAiOiJKV1Q...', '82a59879a507', Array) #1 {main} thrown in /var/www/html/index.php on line 84`

#### JWT? decode?
We google "JWT decode", and it brings us to [jwt.io](https://jwt.io/)<br/>
When we input the cookie, it shows us the value, yet it says `Invalid Signature`<br/><br/>
<img src="./Assets/jwt1.PNG" width="50%" height="50%"><br/><br/>
We find that the format for the code is `JWT::decode($payload, JWK::parseKeySet($jwks), $supportedAlgorithm);`<br/>
Hence, we input the 256-bit-secret as `82a59879a507`<br/>
Now, it is verified<br/><br/>
<img src="./Assets/jwt2.PNG" width="50%" height="50%"><br/><br/>

#### Getting the flag
We use the tool to change `admin` to `true`, and get `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZSwibmFtZSI6ImFzZCJ9.YTbnlIIllCx5UyHp4N-M1f00hDl5erOGmq2V17N8RKg`<br/><br/>
<img src="./Assets/jwt3.PNG" width="50%" height="50%"><br/><br/>
We set it as the cookie, reload the page, and get the flag<br/>

<br/>
> UDCTF{st00p1d_PHP_err0r_mess4ges}