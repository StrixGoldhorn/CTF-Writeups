# Secret Images

Stego<br/>
125 pts<br/>

### Description
We discovered Arasaka operatives sending wierd pictures to each other. It looks like they may contain secret data. Can you find it?<br/><br/>
![Img1](/Tenable2021/Assets/crypted1.png) <br/> 
![Img2](/Tenable2021/Assets/crypted2.png) <br/> 




### Solution
When opening them up in Window's Photos and switching between them back and forth, we realise that they are mostly the same, except for a few pixels<br/>
Hence, we open them up with MediBang Paint Pro, an art software, and place them above one another<br/>
Next, we change the blending of the top layer to "Multiply", and viola, we get the flag<br/>

![Solution](/Tenable2021/Assets/secretimages.png)

> flag{otp_reuse_fail}

> Note: "Difference" would be a better setting for a clearer image
