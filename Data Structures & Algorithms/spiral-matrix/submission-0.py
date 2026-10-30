class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res

        left_bound, right_bound = 0, len(matrix[0]) - 1
        top_bound, bot_bound = 0, len(matrix) - 1

        i, j = 0, 0
        total = len(matrix) * len(matrix[0])
        travel = "right"

        while len(res) < total:
            res.append(matrix[i][j])

            match travel:
                case "right":
                    if j == right_bound:
                        travel = "down"
                        top_bound += 1
                        i += 1
                    else:
                        j += 1

                case "down":
                    if i == bot_bound:
                        travel = "left"
                        right_bound -= 1
                        j -= 1
                    else:
                        i += 1

                case "left":
                    if j == left_bound:
                        travel = "up"
                        bot_bound -= 1
                        i -= 1
                    else:
                        j -= 1

                case "up":
                    if i == top_bound:
                        travel = "right"
                        left_bound += 1
                        j += 1
                    else:
                        i -= 1

        return res