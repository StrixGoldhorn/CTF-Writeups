# Morse Craft

Minecraft<br/>


### Description
You know playing sounds on a 20Hz processor isn't as much fun as I imagined...<br/>
[Challenge source](https://gist.github.com/AndyNovo/c74ba04fbc3cd689774a1d7710af3f08)<br/><br/>
All caps, wrap in UDCTF{}, no underscores or spaces.<br/>
Our mc86 problems introduce a new vanilla Minecraft CPU (java edition).<br/>
It helps to have Java Edition Minecraft but if you don't they can still be solved the old fashioned way.<br/>
Here is a video introducing the architecture and the book to build the CPU:<br/>
[mc86 Intro on YouTube](https://www.youtube.com/watch?v=mqOSgJ0NM_Q)<br/>
[mc86 init book](https://gist.github.com/AndyNovo/657ff15b7614f70e34f7295cb3dd7a8f)<br/>

<br/><br/><br/>

### Solution
First, we beautify the one-liner code.<br/>
We realise that there are 3 types of chunks of code.<br/>
1. 15x "/playsound item.hoe.till master @a ~ ~ ~ 999 1",
2. 5x "/playsound block.bell.use master @p",
3. x,x,x,x,x,
We then replace the 15x `"/playsound item.hoe.till master @a ~ ~ ~ 999 1",` with `-`,<br/>
`5x "/playsound block.bell.use master @p",` with `.`<br/>
and `x,x,x,x,x,` with ` `

We get `-.-. .-. .- ..-. - .. -. --.  -- --- .-. ... .  ..-. --- .-.  - .... .  .-- .. -.` <br/>
When we put it through a morse code decoder, we get the flag<br/>
<br/>
> UDCTF{CRAFTINGMORSEFORTHEWIN}