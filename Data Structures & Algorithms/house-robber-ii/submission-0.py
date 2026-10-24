class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        

        def rob_helper(houses):
            n = len(houses)

            dp = [0] * n

            dp[0] = houses[0]
            if n == 1:
                return dp[0]
            dp[1] = max(houses[1], houses[0])

            for i in range(2, n):
                dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            
            return dp[n-1]
        
        a = rob_helper(nums[:-1])
        b = rob_helper(nums[1:])

        return max(a, b)



        