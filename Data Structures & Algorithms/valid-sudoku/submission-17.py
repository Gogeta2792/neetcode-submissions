class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        box_hash = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]

                if val == ".":
                    continue
                
                if val in row_hash[r] or val in col_hash[c] or val in box_hash[(r//3,c//3)]:
                    return False
                
                row_hash[r].add(val)
                col_hash[c].add(val)
                box_hash[(r//3, c//3)].add(val)

        return True