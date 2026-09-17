class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = float("inf")
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                minVal = min(minVal, nums[left])
                left = mid + 1
            
            elif nums[left] > nums[mid]:
                minVal = min(minVal, nums[mid])
                right = mid - 1
            
            else:
                if nums[left] < minVal or nums[right] < minVal:
                    minVal = min(nums[left], nums[right])
                return minVal
        
        return minVal