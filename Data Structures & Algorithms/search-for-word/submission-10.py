class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def backtracking(r, c, idx):
            if idx == len(word):
                return True
            
            elif not (0 <= r < rows) or \
                not (0 <= c < cols) or \
                (r,c) in seen or \
                board[r][c] != word[idx]:
                return False
            
            seen.add((r,c))
            res = backtracking(r + 1, c, idx + 1) or \
            backtracking(r - 1, c, idx + 1) or \
            backtracking(r, c + 1, idx + 1) or \
            backtracking(r, c - 1, idx + 1)
            seen.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0):
                        return True
        
        return False