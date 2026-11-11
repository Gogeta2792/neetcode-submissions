class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        hashset = set()

        def backtrack(i, j, idx):
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or not board[i][j] == word[idx] or (i,j) in hashset:
                return False

            if idx == len(word) - 1:
                return True

            else:
                hashset.add((i, j))
                res = backtrack(i + 1, j, idx + 1) or backtrack(i - 1, j, idx + 1) or backtrack(i, j + 1, idx + 1) or backtrack(i, j - 1, idx + 1)
                hashset.remove((i,j))

                return res
                
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False