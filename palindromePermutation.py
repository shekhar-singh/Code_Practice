#!/usr/bin/python3

def isPalindrome(inputString):

    inputString = inputString.lower()
    inputString_rev = inputString[::-1]

    if inputString == inputString_rev:
        return True
    else:
        return False
        

def allPalindromeParts(inputString, start, result, temp):

    current = temp[:]
    parts = ''

    for i in range(start, len(inputString)):
        parts = parts + inputString[i]

        if isPalindrome(parts):
            temp.append(parts)

            if i+1 < len(inputString):
                allPalindromeParts(inputString, i+1, result,  temp[:])
            else:
                result.append(temp)

            temp = current



if __name__ == "__main__":

    inputString = input("Enter String : ").strip()
    result = []
    allPalindromeParts(inputString, 0, result,[])

    for i in result:
        print(*i, sep=' ')