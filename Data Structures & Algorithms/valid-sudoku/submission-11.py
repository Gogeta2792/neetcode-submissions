class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                value = board[r][c]

                if value == ".":
                    continue

                if value in row_map[r] or board[r][c] in col_map[c] or board[r][c] in box_map[(r // 3, c // 3)]:
                    return False

                row_map[r].add(value)
                col_map[c].add(value)
                box_map[(r // 3, c // 3)].add(value)

        return True