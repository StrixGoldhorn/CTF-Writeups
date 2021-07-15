# Run-ELF

Minecraft<br/>


### Description
Yo dawg, I heard you liked blue hens...<br/>
[Challenge source](https://gist.github.com/AndyNovo/9b4b1fb5109d0081ae2b65e9ac67c785)<br/><br/>
Our mc86 problems introduce a new vanilla Minecraft CPU (java edition).<br/>
It helps to have Java Edition Minecraft but if you don't they can still be solved the old fashioned way.<br/>
Here is a video introducing the architecture and the book to build the CPU:<br/>
[mc86 Intro on YouTube](https://www.youtube.com/watch?v=mqOSgJ0NM_Q)<br/>
[mc86 init book](https://gist.github.com/AndyNovo/657ff15b7614f70e34f7295cb3dd7a8f)<br/>
Authors: ProfNinja, Gkonos, Daniel<br/>

<br/><br/><br/>

### Solution
Running the command gives us a bunch of 3d pixel-art chickens<br/>
[Here is a video](https://www.youtube.com/watch?v=8wJbwCRihlQ) that one of the organisers posted, that shows all the chickens<br/>
We notice the eyes are different for each chicken<br/>
Taking blue as 0 and black as 1, we come up with some binary numbers<br/>
````
0101 0101 0100 0100 0100 0011 0101 0100 0100 0110 0111 1011 0011 0100 0111 0010 0110 1101 0111 1001 0101 1111 0011 0000 0110 0110 0101 1111 0110 0010 0110 1100 0111 0101 0011 0011 0101 1111 0110 1000 0110 0101 0110 1110 0111 0011 0111 1101
````
Running it through a binary decoder gives us the flag<br/>
<br/>
> UDCTF{4rmy_0f_blu3_hens}