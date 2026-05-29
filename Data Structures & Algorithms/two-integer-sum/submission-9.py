class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # have a seen dictionary to keep track of number -> index
        for i, num in enumerate(nums):
            difference = target - num # calculate the number needed
            if difference in seen: # check to see if we have the index of the number needed
                return [seen[difference], i]
            else:
                seen[num] = i # append current number to dictionary if no number is there

                