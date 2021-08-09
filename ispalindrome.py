def isPalindrome(myString):
    if len(myString) == 0 or len(myString) == 1: return True
    if(myString[0]==myString[len(myString)-1]):
        return isPalindrome(myString[1:-1])
    return False    


myString = 'malayalam'
print(isPalindrome(myString))