class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, cols
        top, bottom = 0, rows

        # First check which row the target would be in
        target_row = 0
        while top <= bottom:
            mid = top + (bottom - top) // 2

            if mid >= rows:
                return False

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                return False
        
        # Then, in the target row, check if the target exists
        selected_row = matrix[target_row]
        while left <= right:
            mid = left + (right - left) // 2

            if mid >= cols:
                return False

            if target == selected_row[mid]:
                return True
            elif target < selected_row[mid]:
                right = mid - 1
            elif target > selected_row[mid]:
                left = mid + 1
            else:
                return False
        
        return False