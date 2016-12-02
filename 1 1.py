import random
from math import *

listShuffled = []


def shuffleList (x):
       while len(x) > 0:
            randElement = random.choice(x)                       
            listShuffled.append(randElement)                    
            userList.remove(randElement)                        
       return listShuffled     

userInput = input("Please enter 6 numbers without commas: ")    
userInput = userInput.replace(' ','')                           
userList = list(userInput)                                      
print(userList)                                                
shuffleList(userList)                                           
print (listShuffled)                                            

