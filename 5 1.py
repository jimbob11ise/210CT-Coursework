from math import *

def subseqLong (x):
    currentSubseq = []                                           #creates empty array to add elements to
    subseqLongest = []                                           #empty array to assign to the longest subsequence

    for i in range(len(x)):                 
        if i < len(x)-1 and x[i] < x[i+1]:                       #if i in within the range of x and the value is smaller than the next
            currentSubseq.append(x[i])                           #adds smaller value to the current subsequence that is being found and removed
        else:
            currentSubseq.append(x[i])                           #part above and here checks the relative length of the sequence being computed
            if len(currentSubseq) > len(subseqLongest):          #checks for longest subsequence length
                subseqLongest = currentSubseq                    #makes the longest variable store the current subsequence
        
            currentSubseq = []                                   #empties the variable for the next sequence

    print ("The longest subsequence is: ", subseqLongest)

userSeqinput = input("Please enter an sequence of numbers: ")
userSeqinput = userSeqinput.replace(" ", "")
userSeqinput = userSeqinput.replace(",", "")
userSeq = list(userSeqinput)
longestFound = subseqLong(userSeq)
