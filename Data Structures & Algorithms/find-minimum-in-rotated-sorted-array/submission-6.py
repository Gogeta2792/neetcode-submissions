class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currMin = float("inf")

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] < nums[mid]: # nums[l:mid] sorted
                currMin = min(currMin, nums[l])
                l = mid + 1
            elif nums[l] > nums[mid]: # nums[mid:] sorted
                currMin = min(currMin, nums[mid])
                r = mid - 1
            else:
                remaining = min(nums[l], nums[r])
                currMin = min(currMin, remaining)
                return currMin