vowels = ["a", "e" ,"i", "o", "u", "A", "E", "I", "O", "U"]
def vowelReplace (x):
    if not x:                                               #checks for empty list
        return x
    elif x[0] in vowels:                                    #checks if the 1st character is in vowel list
        return vowelReplace(x[1:])
    return x[0] + vowelReplace (x[1:])                      #skips first character and moves onto the next element
                    
userWord = input("Please enter a word: ")                   #Takes user input
finalWord = vowelReplace(userWord)                          #calls function
print (finalWord)
