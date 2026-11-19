class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        z_row, z_col = set(), set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    z_row.add(i)
                    z_col.add(j)

        for i in range(ROWS):
            for j in range(COLS):
                if i in z_row or j in z_col:
                    matrix[i][j] = 0
        
        return