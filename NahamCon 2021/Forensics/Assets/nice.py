usb_codes = {"04":"aA", "05":"bB", "06":"cC", "07":"dD", "08":"eE", "09":"fF",
   "0A":"gG", "0B":"hH", "0C":"iI", "0D":"jJ", "0E":"kK", "0F":"lL",
   "10":"mM", "11":"nN", "12":"oO", "13":"pP", "14":"qQ", "15":"rR",
   "16":"sS", "17":"tT", "18":"uU", "19":"vV", "1A":"wW", "1B":"xX",
   "1C":"yY", "1D":"zZ", "1E":"1!", "1F":"2@", "20":"3#", "21":"4$",
   "22":"5%", "23":"6^", "24":"7&", "25":"8*", "26":"9(", "27":"0)",
   "2C":"  ", "2D":"-_", "2E":"=+", "2F":"[{", "30":"]}",  "32":"#~",
   "33":";:", "34":"'\"",  "36":",<",  "37":".>", "4f":">", "50":"<"}

pos = 1
asd = ""
for x in open('keystrokes.txt','r').readlines():
    if pos%2==1:
        t = str(x)[4:6]
        tt = usb_codes.get(t.upper())
        if type(tt)==str:
            print(t,tt[0:1])
            asd = asd + tt[0:1]
    pos+=1

print(asd)
