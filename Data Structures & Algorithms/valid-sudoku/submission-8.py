class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        box_map = collections.defaultdict(set)

        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                value = board[i][j]
                if value == ".":
                    continue

                if (value in row_map[i] or
                    value in col_map[j] or
                    value in box_map[i // 3, j // 3]):
                    return False
                row_map[i].add(value)
                col_map[j].add(value)
                box_map[(i // 3, j // 3)].add(value)
        
        return True