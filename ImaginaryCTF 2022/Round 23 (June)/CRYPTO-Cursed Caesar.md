# Crypto/Cursed Caesar
### FIREPONY57

## Description
Caesar cipher's really easy right?

[encode.py](./Assets/encode.py)

[output.txt](./Assets/output.txt)

## Solution
- Since the algorithm and flag is short, we created [a simple script](./Assets/decode.py) to do mindless brute forcing

```py
charset = "abcdefghijklmnopqrstuvwxyz0123456789!@%^&_{}"
output = [123,101,134,123,125,179,106,102,104,185,103,134,200,114,106,106,184,131,110,188,135,103,197,193,108,188,123,182,143]

shift = 18
res = ""

for c in output:
   found = False
   for n in charset:
      curr = n
      n = ord(n)-97
      n = (n+shift)%128
      if n+97 == c and not found:
         res += curr
         shift = ((n+32)*1337)%27
         found = True
         print(res)

print("- - - COMPLETE - - -")
```

> ictf{0g_c3as3r_c1ph3r_25b4f4}