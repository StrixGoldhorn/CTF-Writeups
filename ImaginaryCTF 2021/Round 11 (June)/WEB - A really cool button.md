# A really cool button

### Description
That button looks VERY tempting. to press.. will you press it?

### Attachments
https://button.max49.repl.co/

### Author
Max49

### Points
50

<br/><br/><br/>

### Solution
When visiting the site, we see a button. Inspecting the source code reveals this:
```HTML
<form action="/noflag.htm" method="POST">
      <input type="submit" value="Go to the flag! It's just a button press away!" />
</form>
```
The button creates a POST request to /noflag.htm<br/><br/>
Hence, we run a curl command to POST a request<br/>
`curl -X POST https://button.max49.repl.co/noflag.htm`<br/><br/>
We receive the following result:
```HTML
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv = "refresh" content = "0; url = /noflag.html" />
  </head>
  <body>
    <!--ictf{f1ag_1n_th3_c0mm3nts!}-->
  </body>
</html>
```
<br/>
> ictf{f1ag_1n_th3_c0mm3nts!}