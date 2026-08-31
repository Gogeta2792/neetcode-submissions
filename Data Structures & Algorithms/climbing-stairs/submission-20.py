class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [1, 1]

        for i in range (2, n + 1):
            DP.append(DP[i-2] + DP[i-1])

        return DP[n]