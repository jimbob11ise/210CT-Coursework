#take input
#sqrt and round down to get nearest sqrt val
#square the val and return that value as nearest perfect square

from math import sqrt

def perfSquare (x):
    if x <= 0:                                          #checks type and val errors
        print ("Please enter an integer")
    elif type(x) != int:
        print ("Please enter an integer")
    else:
        z = pow(x, 0.5)                             #using z as a placeholder
        z = int(z)                                  #rounds to nearest lower integer
        zSquare = (z**2)
        print("The highest and nearest perfect square is " + str(zSquare))
        
        
        
    
