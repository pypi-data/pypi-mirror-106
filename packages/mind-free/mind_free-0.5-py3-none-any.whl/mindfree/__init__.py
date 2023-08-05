def isPalindrome(textString):
    isPalindromeVar = textString.find(textString[::-1])
    if isPalindromeVar == 0:
        my_result = True
    else:
        my_result = False
    return my_result

def checkDuplicates(yourList):
    most = max(set(yourList))
    return most