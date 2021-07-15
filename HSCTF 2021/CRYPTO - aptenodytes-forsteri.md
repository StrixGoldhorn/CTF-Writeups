# crypto/aptenodytes-forsteri
### AC

## Description
Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.
### Attachments
```python
flag = open('flag.txt','r').read() #open the flag
assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)
```
output: `IOWJLQMAGH`

## Solution
Simple Caesar cipher with ROT8

> flag{QWERTYUIOP}