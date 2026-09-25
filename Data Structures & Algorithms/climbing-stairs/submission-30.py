class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                memo[i] = helper(i+1) + helper(i+2)
                return memo[i]
        return helper(0)