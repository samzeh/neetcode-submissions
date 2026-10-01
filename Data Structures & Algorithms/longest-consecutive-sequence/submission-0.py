class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        number = 1
        maxNumber = 1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                number +=1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                maxNumber = max(maxNumber, number)
                number = 1
        maxNumber = max(maxNumber, number)
        return maxNumber
        