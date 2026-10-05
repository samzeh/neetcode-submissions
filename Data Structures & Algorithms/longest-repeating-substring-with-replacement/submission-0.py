class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxLength = 0
        count = {}

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            length = right - left + 1
            maxFreq = max(count.values())

            if length - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            else:
                maxLength = max(maxLength, length)
                right += 1
        
        return maxLength





        