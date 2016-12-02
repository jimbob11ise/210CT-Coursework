from math import *

def binSrch (x, y, z):
    firstVal = 0
    lastVal = len(x)-1
    foundVal = False
    if len(x) == 0:
        foundVal = False
    else:
        while firstVal<=lastVal and not foundVal:                           #while the value exists and isn't found
            middlePnt = (firstVal + lastVal)//2                             #Finds midpoint
            if x[middlePnt]>=y and x[middlePnt]<=z:                         #If the midpoint is between user bounds
                foundVal = True
            else:
                if z < x[middlePnt]:                                        #If not found above, checks if upbound is lower and rectifies midpoint
                    lastVal = middlePnt-1
                else:
                    if y > middlePnt:                                       #if lowbound is too high, rectifies midpoint to reflect
                        firstVal = middlePnt+1
        return foundVal
    
listSrch = [2, 3, 5, 7, 9, 13]
upBound = int(input("Please enter an upper bound: "))
lowBound = int(input("Please enter a lower bound: "))
srchedBool = binSrch (listSrch, lowBound, upBound)
print (srchedBool)
