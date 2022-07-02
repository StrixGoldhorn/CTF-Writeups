# Crypto/Blocks
### Eth007

## Description
[blocks.txt](./Assets/blocks.txt)
```
▄██▄█▄▄█▄██▄▄▄██▄███▄█▄▄▄██▄▄██▄▄████▄██▄██▄▄▄█▄▄██▄██▄▄▄▄██▄▄▄▄▄██▄▄▄██▄██▄█▄██▄██▄▄▄█▄▄███▄█▄█▄███▄▄██▄███▄█▄▄▄██▄▄█▄█▄███▄▄█▄▄█▄█████▄██▄▄▄█▄▄▄██▄▄▄█▄██▄███▄▄██▄▄▄▄█▄███▄▄█▄▄████▄▄█▄█▄█████▄▄██▄▄▄█▄▄███▄▄█▄██▄▄▄█▄▄██▄▄▄█▄▄██▄▄▄▄█▄▄██▄▄▄▄▄▄██▄▄▄▄▄▄██▄▄█▄▄█████▄█
```

## Solution
- Throwing it through CyberChef's `Unique` function, we find that there is `135 ▄130 █`. Seems like it's binary encoded
- Replacing `▄` with 0, and `█` with 1, and splitting it appropriately, we get the following
  
```
01101001 01100011 01110100 01100110 01111011 01100010 01101100 00110000 01100011 01101011 01100010 01110101 01110011 01110100 01100101 01110010 01011111 01100010 00110001 01101110 01100001 01110010 01111001 01011111 00110001 00111001 01100010 01100010 01100001 00110000 00110000 00110010 01111101 1
```

- Converting it to ASCII gives us the flag

> ictf{bl0ckbuster_b1nary_19bba002}