# hack3rm4n_exp0sed

Forensics<br/>
25 + 25 + 50 pts<br/>



### Solution
First, we check the TCP streams</br>
One of the TCP streams that we followed had interesting data</br>
We see that he transferred a few files, namely `butter.jpg`, `compression_info.txt`, and `supersecure.7z`<br/>

<br/><br/><br/>

### First challenge
For the first challenge, we need to filter and follow the FTP-DATA stream which contains `butter.jpg`<br/>
Next, to extract the file, we follow the FTP-DATA's TCP stream, change from ASCII to Raw, and save as a .jpg file<br/>
Then we get the flag<br/>
<img src="/Tenable2021/Assets/butter.jpg" width="50%" height="50%"><br/>

> flag{u_p4ss_butt3r}

<br/><br/><br/>

### Second challenge
For the next challenge, we follow the FTP-DATA's TCP stream for `compression_info.txt`, and find the password to the .7z file<br/>
`The password for the compressed file is "bbqsauce"`
We then extract the files and find the flag<br/>
<img src="/Tenable2021/Assets/pickle_nick.png" width="20%" height="20%"><br/>

> flag{pickl3_NIIICK}

<br/><br/><br/>

### Third challenge
We see another interesting file, titled `dataz`<br/>
Opening it in HxD, we find out that it contains Hex<br/>
Using CyberChef, we find that it is a JPEG file<br/>
Hence, we create a new file and dump the Hex data into it using HxD, then save it as a .jpeg<br/>
<img src="/Tenable2021/Assets/flag3.jpeg" width="50%" height="50%"><br/>
> flag{20_minute_adventure}
