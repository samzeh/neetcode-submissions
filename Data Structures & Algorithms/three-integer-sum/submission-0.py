class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            first = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                summ = first + nums[left] + nums[right]
                if summ == 0:
                    resArray = [first, nums[left], nums[right]]
                    if resArray in result:
                        pass
                    else:
                        result.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif summ > 0:
                    right -= 1
                else:
                    left += 1
        return result
