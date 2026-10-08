class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        dirs = [
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1) # left
        ]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            for dr, dc in dirs:
                area += dfs(dr+r, dc+c)        
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
