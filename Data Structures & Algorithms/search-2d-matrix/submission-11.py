class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        row = -1
        while top <= bottom:
            mid = top + (bottom - top) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
        
        if row == -1 or not (top <= bottom):
            return False
        
        left, right = 0, cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False