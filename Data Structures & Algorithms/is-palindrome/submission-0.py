class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = ""
        for c in s:
            if c.isalnum():
                myString += c.lower()

        left = 0
        right = len(myString)-1
        
        while left < right:
            rightChar = myString[right]
            leftChar = myString[left]
            if rightChar == leftChar:
                right-=1
                left+=1
            else:
                return False
        return True

        