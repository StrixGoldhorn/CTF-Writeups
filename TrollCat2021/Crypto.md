# Selected cryptography challenges in TrollCat 2021 CTF

## Deal Breaking
289 solves

#### Description

Salva is the secretary of the CEO of a ROTech Pvt Ltd. Today is an important day because the CEO is going to a meeting to sign a $13 Million Deal with another company.When Salva went to the office, she finds that the CEO is lying unconscious on his chair. It seems like Salva gave some wrong medicines to the CEO today. But now for the deal to happen, Salva needs to access the CEO's laptop and send the details of the Deal to the Vice President. The laptop was secured with the most modern security service. One has to decrypt a random text to gain access to the laptop.

cnenprgnzbysbeurnqnpur



#### Solution

“ROTech” suggests rotation cipher<br/>
“$13 Million Deal” suggests ROT-13<br/>
Decoding it gets “paracetamolforheadache”

> Flag: Trollcat{paracetamolforheadache}



<br/><br/><br/>
## Lost in Forest
298 solves

#### Description

Rohit one day went on a solo trip on an adventure to Amazon Forest in Brazil. But unfortunately, on his adventure, he got lost in the vast Amazonian forest. His cellphone had no reception and even his compass was not working. After travelling for 6 hours without food and water, he met a tribal man. He was the 64th Tribal Chief of Yanomano tribe of native Amazon. Rohit was delighted to see him and ran straight to him for seeking help. The tribal man agreed to help him but only on ONE condition. That condition was to help the tribal man understand some random text which was etched on a stone tablet for the last 1000 years!!! The text etched on the stone tablet is given below :-
Help Rohit to decode this text. Who knows? It might also help you to find your flag ;)

TWVyY3VyeVZlbnVzRWFydGhNYXJzSnVwaXRlclNhdHVyblVyYW51c05lcHR1bmU=



#### Solution

“64th” suggests Base 64<br/>
Decoding it using any Base 64 converter gives “MercuryVenusEarthMarsJupiterSaturnUranusNeptune”

> Flag: Trollcat{MercuryVenusEarthMarsJupiterSaturnUranusNeptune}



<br/><br/><br/>
## Show Your Dedication
239 solves

#### Description

For the last 11 months, James has been practicing for 5000m Marathon World Championship which is to be organised in Virginia, USA. James has running in his GENES and he has already won many laurels in National Events, but this time he wants to win an international competition. But the day of the race was totally unexpected for him. Unlike normal races, in this race, all the participants were told to run separately and their indvidual time will be recorded. Yet, to his surprise again, there was another rule. The participants were not told about where the finishing line was. The judges handed out a paper to everyone which was encoded in some way and apparantly this text had the destination of the race encoded in it. James is not very good in solving cryptics but he knew that the KEY to this race is RACE itself.
The content of the paper is given below :-
Help James to decode the text and win the race

powv wlck zs JICLQaFRNH



#### Solution

The cipher needs a key, and the key is race<br/>
Using the Vigenere cipher yields the result “your flag is HELLOwORLD”

> Flag: Trollcat{HELLOwORLD}

