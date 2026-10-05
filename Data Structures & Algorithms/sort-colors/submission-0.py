class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2, 1, 1, 2]
        left = 0
        right = len(nums)-1

        while i<=right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i+=1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                i-=1
            else:
                i+=1



        