class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myarr = [0]*len(nums)
        numZero = nums.count(0)


        if numZero > 1:
            return myarr

        elif numZero == 1:
            mult = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    mult *= nums[i]
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    myarr[i] = mult

            return myarr

        else:
            mult = 1
            for num in nums:
                mult *= num
            
        for i in range(len(myarr)):
            myarr[i] = mult // nums[i]
        
        return myarr