# Doubly Deleted Data

Forensics<br/>
260 solves, 330 pts<br/>

### Description
We got a copy of an elusive hacker's home partition and gave it to someone back in HQ to analyze for us. We think the hacker deleted the file with the flag, but before our agent could find it, they accidentally deleted the copy of the partition! Now we'll never know what that flag was. :(<br/>
by Aya Abdelgawad<br/>
*Note: Unable to upload source file as it is too big*

<br/><br/><br/>

### Solution
Open .img file with autopsy<br/>
We then browse through the plaintext files<br/>
We find f0766456.txt, which contains the following<br/>
````
mkdir secret_hacker_stuff
cd secret_hacker_stuff/
nano flag.txt
echo "utflag{d@t@_never_dis@ppe@rs}" > real_flag.txt
rm real_flag.txt
````
<br/>
> utflag{d@t@_never_dis@ppe@rs}