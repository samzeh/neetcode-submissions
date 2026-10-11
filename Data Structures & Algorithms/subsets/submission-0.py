class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res = []
        sol = []

        def backtrack(i):

            if i == len(nums):
                res.append(sol[:]) # append a solution COPY
                return

            # Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res
