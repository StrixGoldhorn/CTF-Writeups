# FlagScript

Web<br/>
Easy, 50 pts<br/>

### Description
[Challenge Link](http://18.194.166.81/flagscript/)



### Solution
Ctrl+U to view source code<br/>
We see an interesting line of code `<script type="text/javascript" src="flagscript.js"></script>`<br/>
Clicking on [flagscript.js](http://18.194.166.81/flagscript/flagscript.js) shows us obfuscated Javascript code<br/>
Using [Online Javascript Beautifier](https://beautifier.io/), we get better looking code<br/>
````Javascript
var _0x44a7 = function(_0x239d1d, _0x2f7f45) {
	_0x239d1d = _0x239d1d - 0x169;
	var _0x2edb04 = _0x2edb[_0x239d1d];
	return _0x2edb04;
};
var _0x26ff06 = _0x44a7;
(function(_0x330f9e, _0x1bb3f1) {
	var _0x50d8d0 = _0x44a7;
	while(!![]) {
		try {
			var _0x597e7a = -parseInt(_0x50d8d0(0x16b)) + parseInt(_0x50d8d0(0x170)) * -parseInt(_0x50d8d0(0x180)) + -parseInt(_0x50d8d0(0x174)) + -parseInt(_0x50d8d0(0x182)) + parseInt(_0x50d8d0(0x17c)) * parseInt(_0x50d8d0(0x175)) + -parseInt(_0x50d8d0(0x16a)) + parseInt(_0x50d8d0(0x17f));
			if(_0x597e7a === _0x1bb3f1) break;
			else _0x330f9e['push'](_0x330f9e['shift']());
		} catch (_0x2e09ef) {
			_0x330f9e['push'](_0x330f9e['shift']());
		}
	}
}(_0x2edb, 0x94600));
var canvasObj = document[_0x26ff06(0x173)](_0x26ff06(0x169)),
	ctx = canvasObj[_0x26ff06(0x181)]('2d');
canvasObj[_0x26ff06(0x16e)] = window['innerHeight'], canvasObj[_0x26ff06(0x172)] = window[_0x26ff06(0x16c)];
var matrix = 'ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789@#$%&^*()';
matrix = matrix[_0x26ff06(0x16d)]('');
var fontSize = 0xa,
	columns = canvasObject[_0x26ff06(0x172)] / fontSize,
	drops = [],
	a = 'S',
	xx = '_',
	ab = '}',
	c = 'C',
	d = 'T',
	e = 'F',
	f = '{',
	g = 'n',
	r = 'c',
	bg = '0',
	fv = 'B',
	i = 't',
	j = '_',
	k = 'a',
	m = 'n',
	n = 'i',
	o = 'c',
	u = 'e',
	jj = 'e',
	q = '_',
	s = 'o',
	kk = 'd',
	flag = a[_0x26ff06(0x16f)](fv, c, d, e, f, g, bg, i, j, k, xx, m, n, o, jj, q, r, s, kk, u, ab);
console[_0x26ff06(0x17a)](flag);
for(var x = 0x0; x < columns; x++) {
	drops[x] = 0x1;
}

function draw() {
	var _0x531c57 = _0x26ff06;
	ctx[_0x531c57(0x183)] = _0x531c57(0x177), ctx['fillRect'](0x0, 0x0, canvasObject[_0x531c57(0x172)], canvasObject[_0x531c57(0x16e)]), ctx[_0x531c57(0x183)] = _0x531c57(0x179), ctx['font'] = fontSize + _0x531c57(0x17e);
	for(var _0x2e7d69 = 0x0; _0x2e7d69 < drops['length']; _0x2e7d69++) {
		var _0x41a070 = matrix[Math[_0x531c57(0x171)](Math[_0x531c57(0x17d)]() * matrix[_0x531c57(0x176)])];
		ctx[_0x531c57(0x17b)](_0x41a070, _0x2e7d69 * fontSize, drops[_0x2e7d69] * fontSize), drops[_0x2e7d69] * fontSize > canvasObject[_0x531c57(0x16e)] && Math[_0x531c57(0x17d)]() > 0.975 && (drops[_0x2e7d69] = 0x0), drops[_0x2e7d69]++;
	}
}
console[_0x26ff06(0x178)](), setInterval(draw, 0x23);
````

Notice these few lines
````Javascript
	a = 'S',
	xx = '_',
	ab = '}',
	c = 'C',
	d = 'T',
	e = 'F',
	f = '{',
	g = 'n',
	r = 'c',
	bg = '0',
	fv = 'B',
	i = 't',
	j = '_',
	k = 'a',
	m = 'n',
	n = 'i',
	o = 'c',
	u = 'e',
	jj = 'e',
	q = '_',
	s = 'o',
	kk = 'd',
	flag = a[_0x26ff06(0x16f)](fv, c, d, e, f, g, bg, i, j, k, xx, m, n, o, jj, q, r, s, kk, u, ab);
````
Replacing each variable with its corresponding character gives us `BCTF{n0t_a_nice_code}`<br/>
Noting that flag format is either FLAG{...} or SBCTF{...}, we add "S" in front of the partial flag we have, to obtain the flag<br/>
>SBCTF{n0t_a_nice_code}
