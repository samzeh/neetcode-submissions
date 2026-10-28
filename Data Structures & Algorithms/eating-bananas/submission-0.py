class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        hour = 0
        
        while left<right:
            mid = (left+right) // 2
            for banana in piles:
                hour += math.ceil(banana/mid)
            
            if hour <= h:
                right = mid
                hour = 0
            else:
                left = mid+1
                hour = 0

        return left