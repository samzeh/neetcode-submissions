class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        dirs = [
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1)  # left
        ]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
            
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))