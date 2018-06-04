import time

def badCharHeuristic(pat, m):
    skip = []
    for k in range(256) : skip.append(m)
    for k in range(m-1) : skip[ord(pat[k])] = m-k-1
    skip = tuple(skip)
    #print(skip)
    return skip


def search(txt,pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    k=m-1
    charCom = 0
    shift = 0
    while k<n:
        j = m-1
        i = k
        while j>=0 and txt[i] == pat[j]:
            charCom = charCom + 1
            j=j-1
            i=i-1
        if j== -1:
            print("matched")
            print("Shift")
            print(k)
            print("CharCom")
            print(charCom)
            return
        k = k+ badChar[ord(txt[k])]
        shift = shift + 1
    print("Shift")
    print(k)
    print("CharCom")
    print(charCom)
    return



def input_Func():
    while 1:
         txt=input("Enter TXT : ")
         pat=input("Enter PAT: ")
         search(txt,pat)

input_Func()