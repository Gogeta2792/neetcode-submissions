class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        target_row = -1

        while top <= bot:
            mid = top + (bot - top) // 2

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                target_row = mid
                break
        
        if not top <= bot:
            return False
        
        left, right = 0, cols - 1
        ROW = matrix[target_row]

        while left <= right:
            mid = left + (right - left) // 2
            
            if target == ROW[mid]:
                return True

            elif target < ROW[mid]:
                right = mid - 1
            elif target > ROW[mid]:
                left = mid + 1

        return False