# Me, Crack

Rev<br/>


### Description
Classic Password Cracking re-imagined for a new generation.<br/>
[Challenge source](https://gist.github.com/AndyNovo/9d9b8ddc5b09e9f3e6203eb3cbfc19a1)<br/><br/>
Our mc86 problems introduce a new vanilla Minecraft CPU (java edition).<br/>
It helps to have Java Edition Minecraft but if you don't they can still be solved the old fashioned way.<br/>
Here is a video introducing the architecture and the book to build the CPU:<br/>
[mc86 Intro on YouTube](https://www.youtube.com/watch?v=mqOSgJ0NM_Q)<br/>
[mc86 init book](https://gist.github.com/AndyNovo/657ff15b7614f70e34f7295cb3dd7a8f)<br/>
Author: ProfNinja

<br/><br/><br/>

### Solution
The instructions are simple:<br/>
1. Create a book with each character of the flag on a page by themselves, and run the program<br/>
2. If there are no errors, the flag is correct<br/>

We take a look at the challange source, and find interesting code<br/>
````
"/scoreboard players set arg1 arith 68","/scoreboard players set arg2 arith 235","/scoreboard players operation arg1 arith *= arg2 arith","/scoreboard players set arg2 arith 17","/scoreboard players operation arg1 arith += arg2 arith","/scoreboard players set arg2 arith 663","/scoreboard players operation arg1 arith %= arg2 arith","/scoreboard players operation arg1 arith -= xval arith","/execute unless score arg1 arith matches 0 run say Failed at page 0"
````
Let's make it neater<br/>
````
"/scoreboard players set arg1 arith 68"
"/scoreboard players set arg2 arith 235"
"/scoreboard players operation arg1 arith *= arg2 arith"
"/scoreboard players set arg2 arith 17"
"/scoreboard players operation arg1 arith += arg2 arith"
"/scoreboard players set arg2 arith 663"
"/scoreboard players operation arg1 arith %= arg2 arith"
"/scoreboard players operation arg1 arith -= xval arith"
"/execute unless score arg1 arith matches 0 run say Failed at page 0"
````
In Python, this would be the equivilant of<br/>
````Python
arg1 = 68
arg2 = 235
arg1 *= arg2
arg2 = 17
arg1 += arg2
arg2 = 663
arg1 %= arg2
# The flag char would thus be chr(arg1)
````
Hence, we extract all arg1 and arg2 integers using Sublime Text, and place them in an array<br/>
We then create a short python script to run and generate the flag<br/>
````Python
arg1=[68,1,8,15,9,12,67,2,19,28,32,62,12,17,33,86]
arg2=[235,17,663,399,19,350,193,178,331,377,365,848,551,17,223,181,63,176,294,139,760,459,37,148,901,793,992,555,522,552,71,1,838,218,144,972,242,84,973,151,81,183,680,305,756,31,19,256]

for i in range(len(arg1)):
    arg1[i]*=arg2[3*i]
    arg1[i]+=arg2[(3*i)+1]
    arg1[i]%=arg2[(3*i)+2]
    print(chr(arg1[i]),end="")
````
And finally, we get the flag<br/>
> UDCTF{MC86_4EVA}