class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jumps = 0

        while r < len(nums) - 1:
            furthest_distance = 0
            for i in range(l, r + 1):
                furthest_distance = max(furthest_distance, i + nums[i])
            
            l = r + 1
            r = furthest_distance
            jumps += 1
        
        return jumps