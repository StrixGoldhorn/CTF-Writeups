# The Reporter

OSINT<br/>
155 solves, 373 pts<br/>

### Description
````
Miss Lola beck has something on her social media account. You are Agent P. find the secret.
Hint : username l.beck
````



### Solution
First, we use [sherlock](https://github.com/sherlock-project/sherlock) to search the username<br/>
We visit the [about.me](https://about.me/l.beck) page and find a hex message `725f37626f6e6e6965`<br/>
Decrypting it gives us `r_7bonnie`<br/><br/>
Once again, we use [sherlock](https://github.com/sherlock-project/sherlock) to search the username<br/>
We find a [Redditor](https://www.reddit.com/user/r_7bonnie) with the username<br/>
Clicking on the post ["Here get something you want"](https://www.reddit.com/user/r_7bonnie/comments/lmrxae/here_get_something_you_want/), we discover a [video](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/DarkCON2021/Assets/r_7bonnie.mp4)<br/>
We discover a QR code in the video<br/><br/>
<img src="https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/DarkCON2021/Assets/r_7bonnieQR.jpg" width="250" height="250"><br/><br/>
Scanning it gives us the flag
> darkCON{os1nst_1s_nic3}
