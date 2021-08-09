#reverse string using recursion

def revString(myString):
    if len(myString) <= 0: return ''
    return revString(myString[1:]) + myString[0] 

myString = 'Hello'

print(revString(myString))