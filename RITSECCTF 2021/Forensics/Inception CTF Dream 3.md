# Inception CTF: Dream 3

Forensics<br/>
186 solves, 200 pts<br/>

### Description
Note: This challenge builds on Inception CTF: Dream 2.<br/>
While the first two steps were easy it’s all hard from here on out, ThePointMan is the most crucial role of the mission he has to be presentable but without giving away our intentions. Use Alternate Dream State to find the flag before the kick.<br/>
Author: Brandon Martin<br/>

<br/><br/><br/>

### Solution
First, we run [Kicks.ps1](./Assets/Inception%20CTF/InceptionCTFRITSEC/Reality/VanChase/Kicks.ps1) with the password `WaterUnderTheBridge`<br/>
We find a [file](./Assets/Inception%20CTF/InceptionCTFRITSEC/Reality/VanChase/dreamwithindream)<br/>
````
You mean, a dream within a dream? NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q=
````
Decoding from base 64 then hex gives us the flag<br/>
<br/>
> RITSEC{F@!!ingElev@tor}