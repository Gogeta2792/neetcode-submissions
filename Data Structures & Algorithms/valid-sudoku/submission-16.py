class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        box_hash = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                num = board[r][c]

                if num == ".":
                    continue

                if num in row_hash[r] or num in col_hash[c] or num in box_hash[(r//3, c//3)]:
                    return False
                
                row_hash[r].add(num)
                col_hash[c].add(num)
                box_hash[(r//3, c//3)].add(num)
        
        return True