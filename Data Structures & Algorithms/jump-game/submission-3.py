class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0

        for i in range(len(nums) - 2, -1, -1):
            distance += 1
            if nums[i] >= distance:
                distance = 0
        
        return nums[0] >= distance