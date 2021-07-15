# Front Pages

General<br/>
39 solves, 493 pts<br/>

### Description
Cover pages or front pages of newspapers and magazines contain the biggest news stories and are designed to grab a person's attention.<br/>
BTW, did you know that the internet has a front page too?<br/>
Flag Format is same : vishwaCTF{}<br/>

<br/><br/><br/>

### Solution
Note: This was basically a simple OSINT challenge<br/>
First, we should note that reddit describes itself as the front page of the internet<br/>
Hence, we google “vishwaCTF” site:reddit.com<br/>
We find that there is a user [u/vishwaCTF](https://www.reddit.com/user/vishwaCTF/comments/), and he had [an interesting post](https://www.reddit.com/user/vishwaCTF/comments/lt1gzm/could_this_be_the_flag_for_a_vishwactf_2021/gouffbd/?context=3)<br/>
<img src="./Assets/redditpost.PNG" width="50%" height="50%"><br/><br/>
Next, we find out that the post was archived in the [wayback machine](https://web.archive.org/web/20210226174949/https://www.reddit.com/user/vishwaCTF/comments/lt1gzm/could_this_be_the_flag_for_a_vishwactf_2021/)<br/>
<img src="./Assets/wayback.PNG" width="50%" height="50%"><br/>

> vishwaCTF{0$dVl_1z_kFV3g_0a3mT0graD}<br/>…<br/>P.S. 18th century French scholars deserve more recognition!<br/>

An old french cipher was the Vigenere Cipher<br/>
At first, automatic decryption on dcode.fr did not yield any results<br/>
However, we guessed and changed the key to vishwaCTF, and viola, we have the flag<br/>

<br/>
> vishwaCTF{0$iNt_1s_oFT3n_0v3rL0okeD}