# Not an AES challenge

## Description
Well sort of

file `notaes.py`, contents pasted below
```py
from Crypto.Cipher import AES
import os

key = os.urandom(16)
nonce = os.urandom(8)
flag = b"ictf{streeeeeeeeeem_ciphers_are_cooooooooooool}"
notflag = b"The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(f"enc = {cipher.encrypt(flag)}")

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(f"dec = {cipher.decrypt(notflag)}")

# enc = b'\x99gW\xcb\xb1(\xa8\xa6@\xca\xedT\x9c\xa6\xeb\x1cH,\x86A\xcbYj|\xb0\x1f PXI\x83\x86\nc7\xb8[\x86\x888\xc7\\D-\x17\xf1\xe7'
# dec = b'\xa4lF\x8d\x8c2\xa8\xba@\xdc\xfbv\x8b\xa2\xe3Y}(\x88{\xda\x10Nq\xa6\x19sfJ\x1b\x87\xf9\x04y4\xa3]\x9a\x936\xcfV\x0b#\x1d\xef\xf5\x83\x91\x0b\x0e\x1d\xd1\xec|\xba\xb8\x08\xb5\xb09r5b\xa40\xb3\x9e\x93\xdd\\\x1b\xe5r\x85@\xf5\x9f\r:\xc6 0\x88\xa6\xfdje\xec\x1dK\x8d\x04\xcfj\t\x19\x0exQ(\xf0\xbaw\xc1\xeb_c\xea\x13\xc0\x884\x80\x82<\\A:q}\xb2}\xf4n\xfa\xf4\x9f\xb9\xe2\x11\xec\xdfP\xfa\xfd\xf3\x1dg)\x9d\x08<\x86@\x99\x90-!\x91\xc1\x87\xe2\xbf!\xdb\xb4X7X\xa4mz\xba\x16\xbb\xc4\x7fNO\xeb\xa5\t\xa6\x18Q|\xd0/\xcbCo2\xfa\xb2K\xd5\x99\x8a\xccG1\xba\xd3\x8c\xe0\xca\x17\xef/A \x95\xc5\xdbf8jx\xc3\xdf\xa5\xcbl\xea\x99\xd9\x89g\x91\x89)o\xcb\xb4\xacJ\x87\x15\x8f1\x0e\xf4~\xeb\xaf\x07\xe8)0\xb9\x83\xbc\x94\xb2\x8fW\x17\xa6\x13\x04\x15\x9c\xd7\x9b\xe7\tU\x9a\xa7Hb\x02\x9fY\xa1+\xc9\n\x16\x0b\xfc\xb0pZ\x00\xdc\xfa)\xa3\xa79\x9f(#A\x9a`\xbbA\xfe\x96DC\x81\x81\x89$\xaeM\x18I\xe2\\\x8a E\xfa\x1e\x88\xb9HnU\xedEzS\xe8\xd7H\xa5\xdd_\xd1L\xa2{q\x90\x19\xe5v\xcf\x83\x1d^\x7f\xa2tqg\xddu3\xbb\xf2\x1c\xfd\xb4s9\xd3C2r\xf1\xe4,\x9d\xd4\x85\x0e>\x86\xcc\xd5\x10\xfe\x98r\xff7`\x80y$`\x85F\xff\x9b\xfc\xacu\xd0YU\x13*\xac\x91\xc21\x9e\xac\xf1\xd7\xa6-\xca{J\xf8\x989\xf2\x975\x16\xe6\xe2\x0b8\x9c\t+\xf7\xb0a\x95lRXe\xb8f\xb3\xe1\x1b\x97E\xd0\xc7HV\xa2\x7f\xcc\x89\xfb\\E\x18\x10\x8bG\x00}o\xe1\x0cn\xc1\xa7y\x84\xde\x96\xf8\xe6U\t\x1ei\xac\xe6q\x13\xf40\xfb\x85%\xbe\x93\xa7\x12^\xbcz\xea\xc8\x14!\xf2\xb0\xa6`m\xed\xedo+\x85\xc8\xec\xf0\xb4\xbfA\x04x\xf6T\xf1\x9e\xdbN}\x1d\x8a\xc84\x1e\x19Y\x19\xf9\x81\xc9\x1c\x91\xc1\xc9\xfbC\x1764\x16\x98\x97\xe0`O\xcb,\x14A\xf34\xf9<\xc0P\x01\xd5+\xd4\xfcyYW\xad\x8c\x08R\xb9^\xd9\x1d\xb0\xe5P\x81H\xab"\xd72:\xc0\xf8K'
```

## Solution
1. notice it uses AES CTR mode
2. "key" can be "found" by XOR-ing known input and known output
3. the "key" (in hex) we get is `f00423adca5bdcd425af8831f9c38e792d49eb1ea8301a14d56d530f393be6d9690c58d734e9e757a8332b42789d9ae1f8682e7eb09c1dd9d17ccc904d1746168444dbffe7fd2c698a15f72586ec644ca34c49a8c1981e16cc7024ff61ef0e607f6811325d9cce57a0987f0a9e33a3e75af4eb522924495f5de615914ec8c4bfd4876589ad708a9c90781509e96d4ff260eef9414db1a3e285d64ffbdd36176b944d09df75d4aa1b3d61cbe960c87d7109a00faa374f4692d76ba6edebbe331f9a87e485ea659a412f49fba2fb15480f1da7ffd6bf0d98edaaa914fde65e03b2988c28f261af566b800dcbc9669b5d55cba3d9f5d1e7777acf7d7161f9f7fa817d30e887310d77bf31c44abb2a626395c3502969bb9448cf8919c44a4624ea3d9b00dee52d2de6edec04c22c68699134e555299e3eeadc680d3a803516369cb22c85b83eb224820f18fd7cc50fa0f63d361ac3065113b51c409b817388da1717f318561b9f8371bd86e0635bebaeb062deec1ddf4515ee594d0ea527dfe888de14b93e3d670ac0f8ac54b28c90b9c20db80e24d8f94ad2fb5a7881c26a4bbc794484c308f700377645ec0ed6c168f226bfa92c76d616a1ecdb252a6d30ed2669114f95634ea2c814f4b2f38c8375683e05cd965171915694f7409ee7cf777ecf159fa6700dd2c9c9151fcd990a58f1e8858394d037610ad874a5f6be6e0978f9bc1469703575d9e3ac7bf8afe9942d37425c73b8e08f122beb5f60208140d71c8f3e21ac44a18e593436dfe72472de3bad3dc28031e5318702a4465bb28c65`
4. XOR-ing it with the cipher text (variable `enc`) gives us the flag

note: the flag seems to be already in the source code

> ictf{streeeeeeeeeem_ciphers_are_cooooooooooool}