class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }

        col_hash = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }

        box_hash = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }

        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                value = board[i][j]
                
                if value == '.':
                    continue

                if (value in row_hash[i] or
                    value in col_hash[j]):
                    return False

                row_hash[i].add(value)
                col_hash[j].add(value)

                if (0 <= i <= 2 and 0 <= j <= 2):
                    if value in box_hash[0]:
                        return False
                    else:
                        box_hash[0].add(value)
                
                if (0 <= i <= 2 and 3 <= j <= 5):
                    if value in box_hash[1]:
                        return False
                    else:
                        box_hash[1].add(value)

                if (0 <= i <= 2 and 6 <= j <= 8):
                    if value in box_hash[2]:
                        return False
                    else:
                        box_hash[2].add(value)

                if (3 <= i <= 5 and 0 <= j <= 2):
                    if value in box_hash[3]:
                        return False
                    else:
                        box_hash[3].add(value)

                if (3 <= i <= 5 and 3 <= j <= 5):
                    if value in box_hash[4]:
                        return False
                    else:
                        box_hash[4].add(value)

                if (3 <= i <= 5 and 6 <= j <= 8):
                    if value in box_hash[5]:
                        return False
                    else:
                        box_hash[5].add(value)

                if (6 <= i <= 8 and 0 <= j <= 2):
                    if value in box_hash[6]:
                        return False
                    else:
                        box_hash[6].add(value)

                if (6 <= i <= 8 and 3 <= j <= 5):
                    if value in box_hash[7]:
                        return False
                    else:
                        box_hash[7].add(value)

                if (6 <= i <= 8 and 6 <= j <= 8):
                    if value in box_hash[8]:
                        return False
                    else:
                        box_hash[8].add(value)

        return True