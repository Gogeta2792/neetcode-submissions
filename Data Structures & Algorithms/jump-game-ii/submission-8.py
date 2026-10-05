class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l, r, = 0, 0

        while r < len(nums) - 1:
            furthest_jump = 0
            for i in range(l, r + 1):
                furthest_jump = max(furthest_jump, i + nums[i])
            steps += 1
            l = r + 1
            r = furthest_jump
        
        return steps