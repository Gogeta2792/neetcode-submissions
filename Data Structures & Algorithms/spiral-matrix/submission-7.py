class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS - 1
        top, bot = 0, ROWS - 1

        res = []
        total = ROWS * COLS
        i, j = 0, 0
        direction = "right"

        while len(res) < total:
            res.append(matrix[i][j])

            match direction:
                case "right":
                    if j == right:
                        top += 1
                        i += 1
                        direction = "down"
                    else:
                        j += 1
                case "down":
                    if i == bot:
                        right -= 1
                        j -= 1
                        direction = "left"
                    else:
                        i += 1
                case "left":
                    if j == left:
                        bot -= 1
                        i -= 1
                        direction = "up"
                    else:
                        j -= 1
                case "up":
                    if i == top:
                        left += 1
                        j += 1
                        direction = "right"
                    else:
                        i -= 1
        
        return res