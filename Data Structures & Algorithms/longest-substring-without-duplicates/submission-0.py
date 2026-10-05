class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLength = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                length = right-left + 1
                maxLength = max(length,maxLength)
                right+=1
            else:
                seen.clear()
                left += 1
                right = left

        return maxLength
        

        