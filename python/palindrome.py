# alghotithm for a palindrome

def is_palindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(is_palindrome("racecar")) 
