# Web/A Little Teapot
### puzzler7

## Description
Find me a teapot, and I'll give you the flag!

http://puzzler7.imaginaryctf.org:2000/

## Solution
- We are given the source code
  ```py
  #!/usr/bin/env python3

  from flask import Flask, Response, request

  from requests import get

  app = Flask(__name__)

  @app.route('/')
  def index():
      return Response(open(__file__).read(), mimetype='text/plain')

  @app.route('/check')
  def check():
      if 'url' not in request.args:
          return "No site found!"
      r = get(request.args['url'])
      if r.status_code == 418:
          return f"That's a teapot! {open('flag.txt').read()}"
      else:
          return "That's not a teapot!"


  app.run('0.0.0.0', 2000)
  ```

  - To get the flag, we need to send a url to a site that returns the response code `418`

  - To do this, we used Pipedream to set up an endpoint that responds with the response code `418` to any request made to the endpoint

  - Hence, we go to `http://puzzler7.imaginaryctf.org:2000/check?url=https://████████████████████████████████.m.pipedream.net`

  - We are then greeted with the flag `That's a teapot! ictf{if_(response.short()_&&_response.stout()):_return_response.tip_over()_&&_response.pour_out()}`

> ictf{if_(response.short()_&&_response.stout()):_return_response.tip_over()_&&_response.pour_out()}
> 