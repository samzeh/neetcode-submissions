class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right] + nums[left] != target:
                right -= 1
            else:
                return [left, right]


        