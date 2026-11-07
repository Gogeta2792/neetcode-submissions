class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        largest = curr

        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            largest = max(largest, curr)
        
        return largest