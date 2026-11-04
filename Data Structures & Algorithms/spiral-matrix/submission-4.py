class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        
        left, right = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1
        total = (right + 1) * (bot + 1)

        i, j = 0, 0
        direction = "right"

        while len(res) < total:
            res.append(matrix[i][j])

            match direction:
                case "right":
                    if j == right:
                        direction = "down"
                        i += 1
                        top += 1
                    else:
                        j += 1

                case "down":
                    if i == bot:
                        direction = "left"
                        j -= 1
                        right -= 1
                    else:
                        i += 1

                case "left":
                    if j == left:
                        direction = "up"
                        i -= 1
                        bot -= 1
                    else:
                        j -= 1

                case "up":
                    if i == top:
                        direction = "right"
                        j += 1
                        left += 1
                    else:
                        i -= 1
        
        return res