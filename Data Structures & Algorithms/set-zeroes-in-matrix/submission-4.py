class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        z_row, z_col = [], []

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    z_row.append(i)
                    z_col.append(j)

        for i in range(ROWS):
            for j in z_col:
                matrix[i][j] = 0
        
        for j in range(COLS):
            for i in z_row:
                matrix[i][j] = 0
        
        return