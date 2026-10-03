class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = steps = 0

        while right < len(nums) - 1:
            farthest_reach = 0
            for i in range(left, right + 1):
                farthest_reach = max(farthest_reach, i + nums[i])
            left = right + 1
            right = farthest_reach
            steps += 1
        
        return steps