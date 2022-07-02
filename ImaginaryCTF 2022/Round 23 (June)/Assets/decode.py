charset = "abcdefghijklmnopqrstuvwxyz0123456789!@%^&_{}"
output = [123,101,134,123,125,179,106,102,104,185,103,134,200,114,106,106,184,131,110,188,135,103,197,193,108,188,123,182,143]

shift = 18
res = ""

for c in output:
   found = False
   for n in charset:
      curr = n
      n = ord(n)-97
      n = (n+shift)%128
      if n+97 == c and not found:
         res += curr
         shift = ((n+32)*1337)%27
         found = True
         print(res)

print("- - - COMPLETE - - -")