class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curr = 0

        for num in nums:
            curr += num
            maximum = max(curr, maximum)
            if curr < 0:
                curr = 0
        
        return maximum