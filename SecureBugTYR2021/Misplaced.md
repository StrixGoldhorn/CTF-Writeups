# Mispalced

Forensics<br/>
Easy, 50 pts<br/>

### Description
[Challenge File](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/SecureBugTYR2021/Assets/file.what)



### Solution
Run `binwalk` on the file<br/>
![](https://github.com/StrixGoldhorn/CTF-Writeups/blob/main/SecureBugTYR2021/Assets/filewhatbinwalk.PNG)
<br/>
Extract the .zip with `binwalk -e file.what`<br/>
We are greeted with a passworded .zip file, so extract it using the password provided (3a24869a641d60c09ceb71af4f99cffc)<br/>
Poking around, we find a document.xml file<br/>
Opening it greets us with xml code<br/>
An interesting section of it is shown below<br/>
````XML
<w:r>
<w:t>SBCTF{</w:t>
</w:r>
<w:r w:rsidRPr="003010F3">
<w:t>n1c3</w:t>
</w:r>
<w:r>
<w:t>_</w:t>
</w:r>
<w:r w:rsidRPr="003010F3">
<w:t>c4rv1n6</w:t>
</w:r>
<w:r>
<w:t>_</w:t>
</w:r>
<w:r w:rsidRPr="003010F3">
<w:t>w3ll</w:t>
</w:r>
<w:r>
<w:t>_</w:t>
</w:r>
<w:r w:rsidRPr="003010F3">
<w:t>d0n3</w:t>
</w:r>
<w:r>
````
Piecing the strings together gives us the flag<br/>
>SBCTF{n1c3_c4rv1n6_w3ll_d0n3}
