# Crypto/One Liner
### puzzler7

## Description
It's a lot harder to put everything on one line in Python than in C, because Python cares about spacing. I've surmised that this must be the reason for the speed difference between the two languages, so I've done my best to minimize my Python in this way.

```py
(lambda:print([s:=list(input(">>> ")),a:=lambda z:[z.pop(),z.reverse()][0],['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no',['no','yes'][a(s)=='}']][a(s)=='i']][a(s)=='p']][a(s)=='c']][a(s)=='u']][a(s)=='t']][a(s)=='t']][a(s)=='f']][a(s)=='e']][a(s)=='{']][a(s)=='g']][a(s)=='h']][a(s)=='t']][a(s)=='e']][a(s)=='n']][a(s)=='l']][a(s)=='a']][a(s)=='p']][a(s)=='c']][a(s)=='s']][a(s)=='i']][a(s)=='o']][a(s)=='d']][a(s)=='m']][a(s)=='n']][a(s)=='e']][a(s)=='a']][a(s)=='o']][a(s)=='s']][a(s)=='n']][a(s)=='r']][a(s)=='e']][a(s)=='a']][a(s)=='s']][a(s)=='h']][a(s)=='t']][a(s)=='c']][a(s)=='o']][a(s)=='g']][a(s)=='l']][a(s)=='n']][a(s)=='e']][a(s)=='i']][a(s)=='a']][a(s)=='c']][a(s)=='l']][a(s)=='a']][a(s)=='l']][a(s)=='p']][a(s)=='m']][a(s)=='s'],'no'][::-1][a(s)=='y']))()
```

## Solution

- Using `Sublime Text`, we isolated the characters, to get `}ipcuttfe{ghtenlapcsiodmneaosnreashtcoglneiaclalpms`

- We notice a pattern of alternating letters. Isolating them, we get two sets of characters, `}putegtnacidnasrahcgnicaps` and `ictf{helpsomeonestoleallm`

- Reversing the first set and appending it to the second set gives us the flag

> ictf{helpsomeonestoleallmyspacingcharsandicantgetup}