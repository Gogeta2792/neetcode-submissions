class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = left = right = 0

        while right < len(nums) - 1:
            biggest_reach = 0
            for i in range(left, right + 1):
                biggest_reach = max(biggest_reach, i + nums[i])
            left = right + 1
            right = biggest_reach
            steps += 1
        
        return steps