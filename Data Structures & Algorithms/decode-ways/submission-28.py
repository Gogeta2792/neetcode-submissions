class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            else:
                memo[i] = (helper(i+1) if s[i] != "0" else 0) + (helper(i+2) if 10 <= int(s[i:i+2]) <= 26 else 0)
                return memo[i]
        return helper(0)