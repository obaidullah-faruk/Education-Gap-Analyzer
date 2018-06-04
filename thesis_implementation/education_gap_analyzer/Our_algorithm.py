import math
import time

def search_Func(txt,pat,n,m,posIndex):
    start=time.time()
    if m%2==0:
        midPoint=int(m/2)
    else:
        midPoint=math.floor(m/2)+1
    isMatch = False
    length=len(posIndex)
    flag=0
    shift=0
    charComparison = 0
    for pos in posIndex:
        k=pos
        l=0
        p=m+k-1
        LastCharPat=m-1
        count=0
        while k<=p:
            charComparison = charComparison + 2
            if (txt[k+1]==pat[l+1]) and (txt[p-1]==pat[LastCharPat-1]):
                k+=1
                l+=1
                p-=1
                LastCharPat-=1
                count+=1
            else:
                 break
        if count==midPoint:
            flag=1
            isMatch = True
            break
        shift=shift+1

    if flag==0:
        isMatch = False
    end=time.time()
    searchTime=end-start
    return charComparison , shift , searchTime , isMatch

def preProcess_Func(txt, pat):
    start=time.time()
    charComparison=0
    shift =0
    searchTime=0
    preProcessTime=0
    isMatch =False
    n=len(txt)
    m=len(pat)
    if m==1:
        return charComparison, shift, preProcessTime, searchTime, isMatch
    i=0
    posIndex=[]
    while i<=(n-m):
        if txt[i]==pat[0]:
            if txt[i+m-1] == pat[m-1]:
                posIndex.append(i)
        i+=1
    end=time.time()
    preProcessTime= end-start
    charComparison, shift, searchTime, isMatch = search_Func(txt,pat,n,m,posIndex)

    return charComparison, shift, preProcessTime, searchTime, isMatch
