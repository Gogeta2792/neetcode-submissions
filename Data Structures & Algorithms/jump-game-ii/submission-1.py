class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]

            min_jumps = float("inf")

            for j in range(1, nums[i] + 1):
                res = helper(i + j)
                if res != float("inf"):
                    min_jumps = min(min_jumps, res + 1)
            
            memo[i] = min_jumps
            return memo[i]

        return helper(0)