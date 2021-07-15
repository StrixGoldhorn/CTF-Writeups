# Mixed Columns

Minecraft<br/>


### Description
I was pleased at how much more I enjoy this cipher in an immersive world.<br/>
[Challenge source](https://gist.github.com/AndyNovo/6e961ce5facd64417543ac9809658085)<br/>
(FORMAT: we're using [5S] and [0O] at the ambiguous spots)<br/><br/>
Our mc86 problems introduce a new vanilla Minecraft CPU (java edition).<br/>
It helps to have Java Edition Minecraft but if you don't they can still be solved the old fashioned way.<br/>
Here is a video introducing the architecture and the book to build the CPU:<br/>
[mc86 Intro on YouTube](https://www.youtube.com/watch?v=mqOSgJ0NM_Q)<br/>
[mc86 init book](https://gist.github.com/AndyNovo/657ff15b7614f70e34f7295cb3dd7a8f)<br/>

<br/><br/><br/>

### Solution
Running the book gives us a few columns of letters<br/><br/>
<img src="./Assets/mixedcol.png" width="70%" height="70%"><br/><br/>
Noting that the flag format is "UDCTF{...}", we figure out that the columns are mixed in the order 6, 7, 3, 5, 2, 4, 1<br/>
Thus, we get each character according to the order, and we are able to get the flag<br/>
<br/>
> UDCTF{7R4NSP0S3_7HE_C0LUMN5}