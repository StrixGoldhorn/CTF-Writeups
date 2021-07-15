# Redeem

Web<br/>
148 solves, 385 pts<br/>

### Description
One of our seller has the flags. and it seems you don't have enough money to buy the same.<br/>
The only way to get money is by redeeming the coupon code. TRY UR LUCK ! https://redeeeem.vishwactf.com/<br/>

<br/><br/><br/>

### Solution
First, we try buying without doing anything, and it notes that we do not have enough money<br/>
Viewing the source code reveals this:<br/>
`<input type="hidden" name="current" value="0">`<br/>
We then change the value from 0 to 10000<br/>
We buy again, and get the flag<br/>
<br/>
> vishwaCTF{@DDed_T0_C@rT_}