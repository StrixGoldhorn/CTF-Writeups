# Numerological

Stego<br/>
100 pts<br/>

### Description
<img src="/Tenable2021/Assets/shield.png" width="20%" height="20%"><br/>



### Solution
First, we binwalk the file<br/>
````
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1200 x 1464, 8-bit/color RGBA, non-interlaced
138           0x8A            Zlib compressed data, best compression
492445        0x7839D         PNG image, 885 x 400, 8-bit/color RGBA, non-interlaced
495277        0x78EAD         TIFF image data, big-endian, offset of first image directory: 8
````

Interesting. Let's extract the PNG image<br/>
<img src="/Tenable2021/Assets/7839D.png" width="50%" height="50%"><br/>
It seems to be a cipher of some kind<br/>

#### Finding the Cipher
Reversing the original image given, we find out that it is actually the coat of arms for the Cistercians<br/>
Searching for "Cistercian cipher" on Google, we find out that the cipher is actually called the "Cistercian Monk Numerals"<br/>

#### Cistercian Monk Numerals
Each "numeral" is divided into 4 parts, the top-left, top-right, bottom-left, and bottom-right<br/>
The top-right is the ones digit, top-left the tens, bottom-right the hundreds, and bottom-left the thousands<br/>
Decoding the numbers gives us `3637 3639 3734 3265 3639 3666 3266 3461 3734 3461 3631 3538`<br/>

#### Further decoding
We remove the spaces in between to form `363736393734326536393666326634613734346136313538`<br/>
Using CyberChef's magic function, we convert it from hex 2 times, to get a link [`git.io/JtJaX`](https://git.io/JtJaX)<br/>
<br/>
Visiting the site gives us the flag<br/>
> flag{th0s3_m0nk5_w3r3_cl3v3r}
