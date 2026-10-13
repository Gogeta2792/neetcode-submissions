class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 and len(board[0]) <= 2:
            return
        
        rows, cols = len(board), len(board[0])

        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def dfs(r,c):
            if not (0 <= r < rows) or \
               not (0 <= c < cols) or \
               board[r][c] != "O":
               return
            
            else:
                board[r][c] = "A"
                for dir_r, dir_c in directions:
                    row, col = dir_r + r, dir_c + c
                    dfs(row, col)
                return

        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "A":
                    board[r][c] = "O"
        
        return
        