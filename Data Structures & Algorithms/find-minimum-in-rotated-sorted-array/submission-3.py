class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        smallest = float("inf")

        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]: # nums[left:mid] sorted
                smallest = min(smallest, nums[left])
                left = mid + 1
            
            elif nums[left] > nums[mid]: # nums [mid:] sorted
                smallest = min(smallest, nums[mid])
                right = mid - 1
            
            else:
                small = min(nums[left], nums[right])
                smallest = min(smallest, small)
                return smallest
        
        return smallest