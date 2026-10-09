class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0

        q = deque()

        dirs = [
            (-1,0), # up
            (1,0), # down
            (0,1), # right
            (0,-1)  # left
        ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            rotted = False
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        rotted = True
            if rotted:
                minutes += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes
