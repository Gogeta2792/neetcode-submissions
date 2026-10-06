class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board or not board[0] or not word:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r,c,idx):
            if idx == len(word):
                return True
            
            if not (0 <= r < rows) or \
               not (0 <= c < cols) or \
               board[r][c] != word[idx]:
               return False
            
            tmp = board[r][c]
            board[r][c] = "."

            res = dfs(r+1,c, idx+1) or \
                dfs(r-1,c, idx+1) or \
                dfs(r,c+1, idx+1) or \
                dfs(r,c-1, idx+1)

            board[r][c] = tmp

            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False