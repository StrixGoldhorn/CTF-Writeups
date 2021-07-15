# We Need An Emulator

Code<br/>
150 pts<br/>

### Description
Attached is some some never-before-seen assembly code routine that we pulled off a processor which is responsible for string decryption. An input string is put into TRX register, then the routine is run, which decrypts the string.

For example, when putting UL\x03d\x1c'G\x0b'l0kmm_ string in TRX and executing this code, the resulting string in TRX is decrypted as 'tenable.ctfd.io'.

A few things we know about this assembly:

There are only two registers, DRX and TRX. These are used to hold variables throughout the runtime.

Operand order is similar to the AT&T syntax ,which has destination operand first and source operand 2nd ie: MOV DRX, "dogs", puts the string "dogs" into DRX register/variable. XOR TRX, DRX, xors the string held in DRX with the string in TRX and stores the result in TRX register/variable.

There are only three instructions that this processor supports:

XOR - XORs the destination string against a source string and stores the result in the destination string operand. The source string operand can be either literal string or string held in a register/variable. Destination operand is always register. XORs all characters against target string characters starting with beginning chars. Below is an example.

  	DRX = "dogs"
  	TRX = "shadow"
  	
  	XOR TRX, DRX

TRX would become \x17\x07\x06\x17ow

MOV - Simply copies the string from a source operand to the destination operand, the source string operand can be either literal or in another register as a variable.
REVERSE - This only takes one operand, and simply reverses the string. ie: if DRX holds "hotdog" then "REVERSE DRX" turns DRX into "godtoh". The operand for this can only be a register.
What we need We need an emulator that can execute the code in the attached file in order to decrypt this string...

GED\x03hG\x15&Ka =;\x0c\x1a31o*5M

If you successfully develop an emulator for this assembly and initialize TRX with this string, execution should yield a final result in the TRX register.



### Solution
There are 3 main functions required, namely `MOV`, `REVERSE`, and `XOR`<br/>
There are only 2 registers, namely `TRX` and `DRX`<br/>
Hence, we decided to create 2 arrays for both the registers, break words into characters, and store them as integers in the array<br/> 
````Python
def word2int(a):
    b=[]
    for i in a:
        b.append(ord(i))
    return b

def int2word(a):
    b=""
    for i in a:
        b+=chr(i)
    return(b)
````
#### MOV
We create a function to copy 1 item from a register to the other<br/>
````Python
def MOV(a, b):
    global DRX, TRX
    if a == 'DRX':
        if b == 'TRX':
            DRX = TRX.copy()
        else:
            DRX = word2int(b)
    elif a == 'TRX':
        if b == 'DRX':
            TRX = DRX.copy()
        else:
            TRX = word2int(b)
    return
````
#### Reverse
We simply reverse the whole list of the given register<br/>
````Python
def REVERSE(a):
    global DRX, TRX
    if a == 'DRX':
        a = DRX[::-1]
        DRX = a
    elif a == 'TRX':
        a = TRX[::-1]
        TRX=a
    return
````
#### XOR
First, we need to know how long the given word is, and then XOR accordingly<br/>
````Python
def XOR(a,b):
    global DRX, TRX
    src=a
    if a == 'DRX':
        a = DRX
        if b == 'TRX':
            b = TRX
        elif b == 'DRX':
            b = DRX
        else:
            b = word2int(b)
    else:
        a = TRX
        if b == 'DRX':
            b = DRX
        elif b == 'TRX':
            b = TRX
        else:
            b = word2int(b)        
    a = list(a)
    b = list(b)
    if(len(b)<len(a)):
        a,b = b,a

    c=b.copy()
    
    for i in range(0, len(a)):
        c[i]=(a[i] ^ b[i])

    if src == 'DRX':
        DRX=c.copy()
    else:
        TRX=c.copy()
````
#### Code
````Python
import codecs


def MOV(a, b):
    global DRX, TRX
    if a == 'DRX':
        if b == 'TRX':
            DRX = TRX.copy()
        else:
            DRX = word2int(b)
    elif a == 'TRX':
        if b == 'DRX':
            TRX = DRX.copy()
        else:
            TRX = word2int(b)
    return

def REVERSE(a):
    global DRX, TRX
    if a == 'DRX':
        a = DRX[::-1]
        DRX = a
    elif a == 'TRX':
        a = TRX[::-1]
        TRX=a
    return

def word2int(a):
    b=[]
    for i in a:
        b.append(ord(i))
    return b

def int2word(a):
    b=""
    for i in a:
        b+=chr(i)
    return(b)

def XOR(a,b):
    global DRX, TRX
    src=a
    if a == 'DRX':
        a = DRX
        if b == 'TRX':
            b = TRX
        elif b == 'DRX':
            b = DRX
        else:
            b = word2int(b)
    else:
        a = TRX
        if b == 'DRX':
            b = DRX
        elif b == 'TRX':
            b = TRX
        else:
            b = word2int(b)        
    a = list(a)
    b = list(b)
    if(len(b)<len(a)):
        a,b = b,a

    c=b.copy()
    
    for i in range(0, len(a)):
        c[i]=(a[i] ^ b[i])

    if src == 'DRX':
        DRX=c.copy()
    else:
        TRX=c.copy()

def main():
    global DRX, TRX
    DRXstring = ""
    TRXstring = "GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"
    DRX = word2int(DRXstring)
    TRX = word2int(TRXstring)
    
    file1 = open('Crypto.txt', 'r')
    content = file1.readlines()
    for line in content:
        line=line[:-1]
        print()
        print(line)
        print("DRX:", DRX)
        print("TRX:", TRX)
        asminstr=line.split(" ")        
        if len(asminstr)==3:
            if asminstr[2]!="DRX" and asminstr[2] != "TRX":
                asminstr[2]=asminstr[2][1:-1]
            
        if asminstr[0]=="MOV":
            MOV(asminstr[1], asminstr[2])
        elif asminstr[0]=="XOR":
            XOR(asminstr[1], asminstr[2])
        elif asminstr[0]=="REVERSE":
            REVERSE(asminstr[1])
        print("DRX:", DRX, int2word(DRX))
        print("TRX:", TRX, int2word(TRX))
        
    print(int2word(TRX))

main()
````
Running the code gives us the flag<br/>
> flag{N1ce_Emul8tor!1}
