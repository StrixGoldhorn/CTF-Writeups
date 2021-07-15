# Invalid

Networking<br/>
142 solves, 394 pts<br/>

### Description
In the previous challenge's file, what was the ip of the person who entered the wrong credentials?

<br/><br/><br/>

### Solution
We filter to look at the SIP stream, and then sort by IP<br/>
We realise that 212.242.33.35 is sending lots of “401 Unauthorized” and “403 Wrong Password” packets to 192.168.1.2<br/>
At first we try 192.168.1.2, but it appears that the accepted answer was 212.242.33.35<br/>
<br/>
> vishwaCTF{212.242.33.35}