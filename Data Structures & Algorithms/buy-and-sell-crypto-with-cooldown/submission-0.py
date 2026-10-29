class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = []

        for _ in range(n):
            temp = [0]*3
            dp.append(temp)

        # [buy, sold, rest]
        dp[0][0] = -prices[0]
        dp[0][1] = float("-inf")
        dp[0][2] = 0

        for i in range(1, n):
            dp[i] = [
                max(dp[i-1][0], dp[i-1][2] - prices[i]), 
                dp[i-1][0]+prices[i], 
                max(dp[i-1][2], dp[i-1][1])
            ]
        
        return max(dp[n-1][1], dp[n-1][2])
         