class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Transpose
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse
        for i in range(rows):
            for j in range(cols // 2):
                matrix[i][j], matrix[i][cols - j - 1] = matrix[i][cols - j - 1], matrix[i][j]