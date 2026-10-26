class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        target_row = 0

        while top <= bot:
            mid = top + (bot - top) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            
            elif target < matrix[mid][0]:
                bot = mid - 1
            
            elif target > matrix[mid][-1]:
                top = mid + 1
        
        if not (top <= bot):
            return False
        
        left, right = 0, cols - 1
        row = matrix[target_row]

        while left <= right:
            mid = left + (right - left) // 2

            if target == row[mid]:
                return True
            
            elif target < row[mid]:
                right = mid - 1
            
            elif target > row[mid]:
                left = mid + 1
        
        return False