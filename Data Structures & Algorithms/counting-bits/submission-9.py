class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n+1):
            dp[i] = dp[i & (i - 1)] + 1
        
        return dp