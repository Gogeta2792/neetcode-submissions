class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum, curr_sum = nums[0], 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            largest_sum = max(largest_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return largest_sum