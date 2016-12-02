from math import *

userNumber = int(input("Please enter an integer"))
noOfzeroes = 0
if type(userNumber) != int:                         #checks type
    print ("Please enter an integer")       
elif userNumber < 0:                             #checks sign
    print("Please enter a positive number")
elif userNumber == 0 :                           #stops zero error
    print("The factorial of 0 is 1")
else :
    pass

def factFinder (userNumber):
    for userNumber in range (2, userNumber+1):
        x = userNumber
        while x > 0:
            if (x // 5) > 0 :
                noOfzeroes +=1
                x = userNumber // 5
                return x            
            else:
                break
                
print("the number of trailing zeroes is" + str(noOfzeroes))
