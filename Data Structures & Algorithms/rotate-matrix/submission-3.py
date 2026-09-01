class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Suppose a 3x3 matrix
        # Transpose
        for r in range(rows): # rows 0, 1 , 2
            for c in range(r + 1, cols):# coordinates that swap (0,1), (0,2), (1,2)
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # Reverse
        for r in range(rows): # rows 0, 1, 2
            for i in range(cols // 2): # for each pass, swap the edges then go inwards once.
                matrix[r][i], matrix[r][cols - i - 1] = matrix[r][cols - i - 1], matrix[r][i]