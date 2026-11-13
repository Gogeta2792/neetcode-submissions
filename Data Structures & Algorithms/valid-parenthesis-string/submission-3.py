class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def helper(i, opened, closed):
            idx = (i, opened, closed)
            if i == len(s):
                return opened == closed
            if closed > opened:
                return False
            if idx in memo:
                return memo[idx]
            
            else:
                if s[i] == "(":
                    memo[idx] = helper(i + 1, opened + 1, closed)
                elif s[i] == ")":
                    memo[idx] = helper(i + 1, opened, closed + 1)
                elif s[i] == "*":
                    memo[idx] = helper(i + 1, opened + 1, closed) or \
                                helper(i + 1, opened, closed + 1) or \
                                helper(i + 1, opened, closed)

                return memo[idx]
                
        return helper(0, 0, 0)