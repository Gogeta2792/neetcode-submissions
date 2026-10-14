class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return
        
        rows, cols = len(matrix), len(matrix[0])

        # Transpose:
        for r in range(rows):
            for c in range(r + 1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # Reverse:
        for r in range(rows):
            for c in range(cols // 2):
                matrix[r][c], matrix[r][cols - 1 - c] = matrix[r][cols - 1 - c], matrix[r][c]
        
        return