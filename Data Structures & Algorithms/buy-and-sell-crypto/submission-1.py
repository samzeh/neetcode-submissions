class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        dp = [0]*n

        dp[0] = prices[0]

        for i in range(1, n):
            dp[i] = min(dp[i-1], prices[i])
        
        for i in range(n):
            profit = prices[i] - dp[i] 
            max_profit = max(max_profit, profit)
        
        return max_profit

        