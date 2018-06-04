import time
# charComparison, shift, preProcessTime, searchTime , isMatch
NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    start=time.time()

    badChar = [-1]*NO_OF_CHARS
    count = 0
    #astric = size + 1
    for i in range(size):
        if i == size:
            for j in size-1:
                if badChar[ord(string[i])] == ord[string[j]]:
                    badChar[ord(string[i])] = j
                    count = 1
            if count == 0:
                badChar[ord(string[i])] = size
        else:
            badChar[ord(string[i])] = i
    #badChar[ord(string[size+1])] = size
    end=time.time()
    #print("Execution time in preprocessing Phase : ", end-start)
    preProcessTime = end - start
    return badChar ,preProcessTime

def BMsearch(txt, pat):
    m = len(pat)
    badChar , preProcessTime = badCharHeuristic(pat, m)

    start=time.time()
    isMatch = False
    n = len(txt)
    pos = 0
    shift=0
    charComparison=0
    while(pos <= n-m):
        j = m-1

        while j>=0 and pat[j] == txt[pos+j]:
            charComparison=charComparison+1
            j -= 1

        if j<0:
            #print("Pattern occur at position = {}".format(pos))
            #print("Total shift = {}".format(shift))
            #print("Total Character Comparison = {}".format(charComparison))
            isMatch = True
            try:
                pos += (m-badChar[ord(txt[pos+m])] if pos+m<n else 1)
                charComparison = charComparison + 1
            except:
                break
        else:
            try:
                pos += max(1, j-badChar[ord(txt[pos+j])])
                charComparison = charComparison + 1
            except:break
        shift = shift + 1

    end=time.time()
    #print("Execution time in searching phase : ",end-start)
    searchTime = end-start
    return charComparison, shift, preProcessTime, searchTime , isMatch


