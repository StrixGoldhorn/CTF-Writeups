# Read

Reverse<br/>
123 solves, 406 pts<br/>

### Description
Reading is the best way to solve a challenge
[File](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/DarkCON2021/Assets/read.pyc)



### Solution
First, we run it through [uncompyle6](https://pypi.org/project/uncompyle6/) to obtain the [original code](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/DarkCON2021/Assets/darkconcursedreverse.py)<br/>
We discover an interesting section of the code

````Python
babababa = 'you-may-need-this-key-1337'

.
.
.


def lababa(lebula):
    alalalalalalal = [
     73, 13, 19, 88, 88, 2, 77, 26, 95, 85, 11, 23, 114, 2, 93, 54, 71, 67, 90, 8, 77, 26, 0, 3, 93, 68]
    result = ''
    for belu in range(len(alalalalalalal)):
        if lebula[belu] != chr(alalalalalalal[belu] ^ ord(babababa[belu])):
            return 'bbblalaabalaabbblala'
        b2a = ''
        a2b = [122, 86, 75, 75, 92, 90, 77, 24, 24, 24, 25, 106, 76, 91, 84, 80, 77, 25, 77, 81, 92, 25, 92, 87, 77, 80, 75, 92, 25, 74, 77, 75, 80, 87, 94, 25, 88, 74, 25, 95, 85, 88, 94]
        for bbb in a2b:
            b2a += chr(bbb ^ 57)
        else:
            return b2a
````

<br/>

Next, we create a [script](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/DarkCON2021/Assets/darkconreverse.py) to decode `alalalalalalal` <br/>

<br/>

````Python
alalalalalalal = [73, 13, 19, 88, 88, 2, 77, 26, 95, 85, 11, 23, 114, 2, 93, 54, 71, 67, 90, 8, 77, 26, 0, 3, 93, 68]
result = ''
babababa = 'you-may-need-this-key-1337'
for belu in range(len(alalalalalalal)):
    result += chr(alalalalalalal[belu] ^ ord(babababa[belu]))
print(result)
````

Running the script gives us the flag
> darkCON{0bfu5c4710ns_v5_4n1m4710ns}
