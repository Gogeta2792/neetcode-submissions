class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        box_hash = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                value = board[r][c]

                if value == ".":
                    continue

                if (value in row_hash[r]) or \
                (value in col_hash[c]) or \
                (value in box_hash[(r // 3, c // 3)]):
                    return False

                row_hash[r].add(value)
                col_hash[c].add(value)
                box_hash[(r // 3, c // 3)].add(value)

        return True