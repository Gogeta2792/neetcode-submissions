class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS - 1
        top, bot = 0, ROWS - 1

        res = []
        i, j = 0, 0
        direction = "right"

        while len(res) < (ROWS * COLS):
            res.append(matrix[i][j])

            match direction:
                case "right":
                    if j == right:
                        i += 1
                        direction = "down"
                        top += 1
                    else:
                        j += 1

                case "down":
                    if i == bot:
                        j -= 1
                        direction = "left"
                        right -= 1
                    else:
                        i += 1

                case "left":
                    if j == left:
                        i -= 1
                        direction = "up"
                        bot -= 1
                    else:
                        j -= 1

                case "up":
                    if i == top:
                        j += 1
                        direction = "right"
                        left += 1
                    else:
                        i -= 1
        
        return res