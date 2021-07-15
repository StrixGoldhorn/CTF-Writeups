# All of Web Challenges involving the DocJones site
### [Challenge link](http://167.71.246.232/)

# Stay away from creepy crawlers
Web<br/>
25 pts<br/>
### Solution
Crawlers visit /robots.txt of a site<br/>
We visit /robots.txt and find the flag
````
User-agent: *
Disallow: /admin/
# flag{mr_roboto}
````
<br/>
> flag{mr_roboto}

<br/><br/><br/>

# Source of all evil
Web<br/>
25 pts<br/>
### Solution
Hit ctrl+u or F12 to view the source code to get the flag<br/>
> flag{best_implants_ever}

<br/><br/><br/>

# Can't find it
Web<br/>
25 pts<br/>
### Solution
Visit any page that doesn't exist to get the flag<br/>
> flag{404_oh_no}

<br/><br/><br/>

# Headers for you inspiration
Web<br/>
25 pts<br/>
### Solution
Hit F12 to bring up the Developer Console, and click on the Networks tab<br/>
Reload the page<br/>
Under the Networks tab, click on the website's link to view the headers, the flag is there<br/>
> flag{headersftw}

<br/><br/><br/>

# Show me what you got
Web<br/>
25 pts<br/>
### Solution
Once again, view the source code<br/>
We realise that the image is stored in `/images/doc_jones.png`<br/>
Exploring the `/images/` folder, we realise there is another file, `aljdi3sd.txt`<br/>
Click on it to get the flag<br/>
> flag{disable_directory_indexes}

<br/><br/><br/>

# Certificate of authenticity
Web<br/>
25 pts<br/>
### Solution
Add `https://` to the front of the site<br/>
Click on "Not secure" on the left of the address bar, then view certificate to get the flag<br/>
> flag{disable_directory_indexes}

<br/><br/><br/>

# Ripper Doc
Web<br/>
50 pts<br/>
### Solution
Visit [certified_rippers.php](https://167.71.246.232/certified_rippers.php)<br/>
Change the cookie of `authenticated` from `false` to `true`, and reload the page to get the flag<br/>
> flag{messing_with_cookies}

<br/><br/><br/>

# Follow the rabbit hole
Web<br/>
100 pts<br/>
### Solution
Visit [rabbit_hole.php](http://167.71.246.232:8080/rabbit_hole.php)<br/>
Notice that it adds a GET request `?page=cE4g5bWZtYCuovEgYSO1`<br/>
The content of the page is an array of an integer and a string, along with alphanumeric characters<br/>
Example: `[513, '71'] 4O48APmBiNJhZBfTWMzD`<br/>
We try sending a GET request for page, using the alphanumeric characters, and get another similarly formatted page<br/>
Hence, we create a [script](/Tenable2021/Assets/rabbitpt1.py) to acquire and create an array of the array in the page<br/>

````Python
import requests
import urllib.request
import time

urlbase = 'http://167.71.246.232:8080/rabbit_hole.php?page='
combi = []
s = ['','cE4g5bWZtYCuovEgYSO1']

for i in range(0,1582):
    time.sleep(0.01)
    url = str(urlbase+str(s[1]).strip())
    print(i,":",url)
    r = requests.get(url)
    s = r.text.splitlines()
    ts = s[0][1:-1]
    t=list(ts.split(", "))
    t1=t[1]
    t1=t1[1:-1]
    t[1]=t1
    combi.append(t)
print("DONE: ", combi)
````

Next, we realise that the array given in the page is formmated such that the integer is the position of the string in another not-yet-created string<br/>
Hence, we create a [script](/Tenable2021/Assets/rabbitpt2.py) to sort the strings given<br/>

````Python
extracted=[]
#Whole array captured is available in the source file under /Assets/rabbitpt2.py

extracted.sort(key = lambda x:int(x[0]))
amaze = ''

for i,j in extracted:
    amaze += j
print(amaze)
````

We get a [string of hex numbers](/Tenable2021/Assets/rabbit.txt)<br/>
Searching the first few hex numbers, we realise that it is a png file<br/>
Hence, we create a new file in HxD Hex Editor, and paste the hex numbers, and save it as a .png to get the flag<br/>
![flag](/Tenable2021/Assets/followrabbithole.png)<br/>
> flag{automation_is_handy}
