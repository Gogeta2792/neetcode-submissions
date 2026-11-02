class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        MIN = nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[l] < nums[mid]: # left half is sorted
                MIN = min(MIN, nums[l])
                l = mid + 1
            
            elif nums[l] > nums[mid]:
                MIN = min(MIN, nums[mid])
                r = mid - 1
            
            else:
                return min(MIN, nums[l], nums[r])
            
        return MIN