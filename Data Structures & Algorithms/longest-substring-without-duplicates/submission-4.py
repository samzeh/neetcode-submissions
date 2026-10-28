class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxString = 0
        mySet = set()

        while right < len(s):
            if s[right] not in mySet:
                mySet.add(s[right])
                right += 1
                maxString = max(maxString, right-left)
            else:
                while s[right] in mySet:
                    mySet.remove(s[left])
                    left+=1
        
        return maxString

        