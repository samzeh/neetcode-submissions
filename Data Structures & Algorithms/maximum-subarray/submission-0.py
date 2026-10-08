class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxx = nums[0]

        for num in nums[1:]:
            curr = max(curr+num, num)
            maxx = max(maxx, curr)
        
        return maxx

        