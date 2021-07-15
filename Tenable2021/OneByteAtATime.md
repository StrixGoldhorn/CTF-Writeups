# One byte at a time

Misc<br/>
50 pts<br/>



### Solution
The server gives a hex number everytime you enter a character<br/>
We know that the flag format is `flag{...}`, hence we try the characters `f`, `l`, `a`, `g`, and `{` first<br/>
We also note that each time we try a character, there are 3 different results<br/>


| Actual Char |  Ouput Hex        | Actual Hex |
|:-----------:|-------------------|:----------:|
| f           |  0x11, 0x64, 0x76 | 0x66       |
| l           |  0x1b, 0x63, 0x7c | 0x6c       |
| a           |  0x16, 0x63, 0x71 | 0x61       |
| g           |  0x10, 0x65, 0x77 | 0x67       |
| {           |  0x0c, 0x79, 0x6b | 0x7b       |

<br/>
We notice a pattern: When XOR-ed with 0x77, 0x02, or 0x10, the output hex produces the actual hex (and vice versa)<br/>
Hence, we continue XOR-ing the numbers we get from the server, and end up with the flag

> flag{f0ll0w_th3_whit3_r@bb1t}
