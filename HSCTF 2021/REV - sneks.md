# rev/sneks
### hmmm

## Description
https://www.youtube.com/watch?v=0arsPXEaIUY

### Downloads
[output.txt](Assets/sneks/output.txt)
[sneks.pyc](Assets/sneks/sneks.pyc)

## Solution
First, we decompile it using uncompyle6 to see the [source code](Assets/sneks/sneks.py)<br/>
We realise that there is no randomness involved, and when we input `flag{` character by character, it throws the same result as the first few integers in [output.txt](Assets/sneks/output.txt)<br/>
Hence, we create a [short python script to brute-force the flag](Assets/sneks/solve.py)

> flag{s3qu3nc35_4nd_5um5}