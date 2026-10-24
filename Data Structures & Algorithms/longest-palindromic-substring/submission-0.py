class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""

        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)

            if len(odd) > len(longest):
                longest = odd
            
            if len(even) > len(longest):
                longest = even
        
        return longest


        