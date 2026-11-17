class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or not board[i][j] == "O":
                return
            
            else:
                board[i][j] = "A"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
                return

        for i in range(ROWS):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][COLS - 1] == "O":
                dfs(i, COLS - 1)

        for j in range(COLS):
            if board[0][j] == "O":
                dfs(0,j)
            if board[ROWS - 1][j] == "O":
                dfs(ROWS - 1,j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"
        
        return