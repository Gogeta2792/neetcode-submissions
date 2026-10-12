class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        biggest = nums[0]
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            biggest = max(biggest, curr)
        
        return biggest