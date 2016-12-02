from math import *

def checkPrime (n):
    if n <=0 :
        print ("Please enter a positive integer")
    elif n == 1 :
        print ("Please enter a number that is larger than one. It is a special case, but not a prime.")
    else:
        for i in range (2, n-1) :
            if (n%i) == 0:
                return False
        return True
                    
               
userNum = int(input("Please enter a number to check whether or not it is prime: "))
print (checkPrime(userNum))

        
        
    
