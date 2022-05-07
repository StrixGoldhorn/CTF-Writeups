# web/Low Ceiling
### 838 pts, 40 solves

## Description
APOCALYPSE members frequent this server but we dont know what for. Help us find out what its for.

The URL for this challenge: http://chals.cyberthon22f.ctf.sg:40301/

## Solution
Entering the site and poking around yields nothing much, so we visit `/robots.txt`

`/robots.txt` contents:
```
User-agent: *
Disallow:dev
```

Since it disallows dev, obviously the next logical step would be to visit it, because rules are meant to be broken, and we are not web scrapers.

Visiting `/dev` gives us a download to a zip file, unzipping it yields us `index.js`

`index.js` contents:
```js
const path              = require('path');
const express           = require('express');
const router            = express.Router();

router.get('/', (req, res) => {
	secret = req.headers["secret-header"];
    if (secret == "admin"){
    	return res.sendFile(path.resolve('views/admin.html'));
    }
    return res.sendFile(path.resolve('views/index.html'));
});

router.get('/robots.txt', (req, res) => {
    res.type('text/plain');
    res.send("User-agent: *\nDisallow:dev");
});

router.get('/dev', (req, res) => {
	return res.sendFile(path.resolve('dev/source.zip'));
})

module.exports = router;
```

note this interesting chunk of code:
```js
secret = req.headers["secret-header"];
    if (secret == "admin"){
    	return res.sendFile(path.resolve('views/admin.html'));
    }
```

We need to send a request to `/`, with `secret-header: admin` in its header.

Throwing it through Postman gives us the response with the flag.

```html
<html>

<head>
	<title></title>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
	<meta name='author' content='XD'>
	<link rel="stylesheet" type="text/css" href="static/css/main.css">
</head>

<body>
	<div>
		<h1 id="output">Cyberthon{l0w_ceiling_w4tch_ur_head_a6243746643baf3d}</h1>
	</div>
</body>

</html>
```

> Cyberthon{l0w_ceiling_w4tch_ur_head_a6243746643baf3d}