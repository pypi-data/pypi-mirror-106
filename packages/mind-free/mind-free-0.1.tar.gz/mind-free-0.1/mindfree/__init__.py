def isPalindrome(txt):
    isPalindromeVar = txt.find(txt[::-1])
    return isPalindromeVar

def checkDuplicates(myList):
    most = max(set(myList), key=myList.count)
    return most