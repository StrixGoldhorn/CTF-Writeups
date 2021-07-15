# Inception CTF: Dream 2

Forensics<br/>
199 solves, 225 pts<br/>

### Description
Note: This challenge builds off Inception CTF: Dream 1,<br/>
Unfortunately, the subconscious isn’t enough for this mission, we have to kidnap Fischer we need to go further into the system of the mind. Use the flag found to edit the PowerShell script, entering the Flag in line three in-between the single quotes. Run the PowerShell script and wait for it to complete its actions.<br/>

<br/><br/><br/>

### Solution
First, we unzip [VanChase.7z](./Assets/Inception%20CTF/InceptionCTFRITSEC/Reality/VanChase.7z) with the password `Dreamland`<br/>
We find a file named [Kidnap.txt](./Assets/Inception%20CTF/InceptionCTFRITSEC/Reality/VanChase/Kidnap.txt)<br/>
````
An idea is like a virus, resilient, highly contagious. 
52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d
````
Converting it from hex gives us the flag<br/>
<br/>
> RITSEC{WaterUnderTheBridge}