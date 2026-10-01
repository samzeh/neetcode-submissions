class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = nums.count(0)
        res = []
        prod = 1

        if numZeros > 1:
            return [0]*len(nums)

        elif numZeros == 1:
            for num in nums:
                if num != 0:
                    prod *= num
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
            
        else:
            for num in nums:
                prod *= num
            for num in nums:
                res.append(prod//num)
            return res
