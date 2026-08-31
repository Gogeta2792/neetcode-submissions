class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Store top left
                tmp = matrix[top][left + i]
                
                # Bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # tmp to top right
                matrix[top + i][right] = tmp
            
            left += 1
            right -= 1