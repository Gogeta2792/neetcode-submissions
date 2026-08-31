class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(num, n):
            if num in memo:
                return memo[num]
            if num < n:
                memo[num] = helper(num + 1, n) + helper(num + 2, n)
                return memo[num]
            if num > n:
                return 0
            if num == n:
                return 1


        count = helper(0, n)

        return count