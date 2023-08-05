def isPalindrome(some):
    isPalindromeVar = some.find(some[::-1])
    return isPalindromeVar

def checkDuplicates(myList):
    most = max(set(myList), key=myList.count)
    return most