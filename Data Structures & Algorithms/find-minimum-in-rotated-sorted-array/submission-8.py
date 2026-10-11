class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_ele = float("inf")

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] < nums[mid]: # nums[l:mid] is sorted
                min_ele = min(min_ele, nums[l])
                l = mid + 1
            elif nums[l] > nums[mid]: # nums[mid:] is sorted
                min_ele = min(min_ele, nums[mid])
                r = mid - 1
            else:
                return min(min_ele, nums[l], nums[r])
        
        return min_ele