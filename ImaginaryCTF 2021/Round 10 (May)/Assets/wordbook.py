from pwn import *
import string

def exploit():
    chrlist = string.printable
    chrenc = ""

    p = remote("oreos.imaginary.ml", 10069)
    res = p.recv().decode()
    # print(res)
    encflag = res[17:52]
    
    for i in chrlist:
        p.sendline(str(i))
        res = p.recv().decode()
        print(f'New: {i} | {res[12]}', end="\r")
        chrenc += res[12]

    print("-----| COMPLETED WORDBOOK |-----")
    print(chrlist)
    print(chrenc)
    print("-----| DECRYPTING |-----")

    pt = ""
    for i in encflag:
        pt += chrlist[chrenc.index(i)]
    print("Flag:", pt)

exploit()