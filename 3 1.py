sentRev = []
userSentence = input("Please enter a sentence to reverse: ")
userSentence = userSentence.split()                 #splits user input into an array
def reverseSentence (x):
    while len(x) > 0:
        lastElement = userSentence[-1]              #selects last element in array
        sentRev.append(lastElement)                 #adds last element into empty array
        userSentence.remove(lastElement)            #removes from original array
    return sentRev 



reverseSentence(userSentence)
sentRev = " ".join(sentRev)                         #joins it as a sentence using spaces
print (sentRev)
