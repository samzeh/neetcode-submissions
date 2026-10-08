class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        dir = [
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1), # left
        ]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in dir:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands

