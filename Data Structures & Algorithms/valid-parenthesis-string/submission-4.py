class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def helper(i, balance):
            idx = (i, balance)
            if i == len(s):
                return balance == 0
            if balance < 0:
                return False
            if idx in memo:
                return memo[idx]
            
            else:
                if s[i] == "(":
                    memo[idx] = helper(i + 1, balance + 1)
                elif s[i] == ")":
                    memo[idx] = helper(i + 1, balance - 1)
                elif s[i] == "*":
                    memo[idx] = helper(i + 1, balance + 1) or \
                                helper(i + 1, balance - 1) or \
                                helper(i + 1, balance)

                return memo[idx]
                
        return helper(0, 0)