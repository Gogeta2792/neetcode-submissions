class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            dp[i] = (dp[i+1] if s[i] != "0" else 0) + (dp[i+2] if 10 <= int(s[i:i+2]) <= 26 else 0)
        
        return dp[0]