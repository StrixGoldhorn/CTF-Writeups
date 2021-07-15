# Send License

Web<br/>
Easy, 50 pts<br/>

### Description
"We have bought a service but unfortunately we lost the license key of it we are willing to give you a flag at the exchange of the key.
From what we remember it was based on windows 95 oem algorithm.
We bought the service at july 3rd of 1999.

send you'r keys here: http://IP:3000/?license=your-KEY"<br/>
https://ch1.sbug.se	<br/>

<br/><br/><br/>

### Solution
We find how the keys were generated<br/>
The keyas are in the format XXXXX-OEM-XXXXXXX-XXXXX<br/>
The first section is the Julian Day + Last 2 digits of year<br/>
The second section is always "OEM"<br/>
The third section has to start with 2 zeros, followed by a number which sum of digits is divisible by 7<br/>
The last section can be anything<br/>
Hence, we use `18499-OEM-0007777-00001` as the key<br/>
<br/>
> SBCTF{CR4CK1NG_95_W4S_N0T_TH4T_H4RD}