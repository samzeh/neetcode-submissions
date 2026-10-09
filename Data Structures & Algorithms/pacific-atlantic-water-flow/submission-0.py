class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        
        pacific = set()
        atlantic = set()

        dirs = [
            (-1,0), # up
            (1,0), # down
            (0,1), # right
            (0,-1)  # left
        ]
        
        def dfs(r, c, o):
            if (r, c) in o:
                return
            o.add((r, c))

            for dr, dc in dirs:
                nr, nc = dr+r, dc+c

                if nr >= 0 and nr < row and nc >=0 and nc < col and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, o)
        
        # Pacific: top row
        for c in range(col):
            dfs(0, c, pacific)

        # Pacific: left column
        for r in range(row):
            dfs(r, 0, pacific)

        # Atlantic: bottom row
        for c in range(col):
            dfs(row-1, c, atlantic)

        # Atlantic: right column
        for r in range(row):
            dfs(r, col-1, atlantic)

        result = []

        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append((r,c))
        
        return result


        