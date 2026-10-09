class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        dirs = [
            (-1,0), # up
            (1,0), # down
            (0,1), # right
            (0,-1)  # left
        ]
        
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    if board[r][c] == 'O':
                        q.append((r,c))
                        board[r][c] = 'S'        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and board[nr][nc] == 'O':
                    q.append((nr, nc))
                    board[nr][nc] = 'S'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        