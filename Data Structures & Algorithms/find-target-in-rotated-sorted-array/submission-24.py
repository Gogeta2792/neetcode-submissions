class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid

            elif nums[left] < nums[mid]: # nums is sorted
                if target < nums[left] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            elif nums[left] > nums[mid]: # nums[mid:] is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                return right if nums[right] == target else -1