# SETI

Misc<br/>
At least 14 solves, 150 pts<br/>

### Description
Our satellite dish recieved this transmission from Alpha Centuri. Can you decode it?<br/>
[File](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/Tenable2021/Assets/tx.wav)



### Solution
Opening the file in Audacity and switching to spectrogram, we can see what looks like data being transmitted <br/>

Using the `file` command in UNIX, we get this:<br/>
````
$ file tx.wav
tx.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
````

Now, time for some background knowledge. Satellites sent to explore the wonders of space usually use a lower baud rate.<br/>

How is this related to the challenge?<br/>
We use minimodem to read the data, but to do so, we first need to change the file extension from `.wav` to `.s16` (as it is 16 bit)<br/>
Then, we start from the lower baud rates, RTTY and TDD at 45.45 bps. This unfortunately yields no result.<br/>
Yet, we should always persevere onwards. Using Bell103 at 300 bps, the flag magically appears.<br/>
````
$ minimodem -f tx.s16 300
### CARRIER 300 @ 1250.0 Hz ###
flag{our_technology_is_immaculate}

### NOCARRIER ndata=35 confidence=2.414 ampl=0.992 bps=300.00 (rate perfect) ###
````
> flag{our_technology_is_immaculate}
