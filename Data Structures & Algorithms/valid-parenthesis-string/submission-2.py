class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def backtrack(i, opened, closed):
            if closed > opened:
                return False
            elif i == len(s):
                return opened == closed
            state = (i, opened, closed)
            if state in memo:
                return memo[state]

            else:
                if s[i] == "(":
                    memo[state] = backtrack(i + 1, opened + 1, closed)
                elif s[i] == ")":
                    memo[state] = backtrack(i + 1, opened, closed + 1)
                elif s[i] == "*":
                    memo[state] = backtrack(i + 1, opened, closed) or backtrack(i + 1, opened + 1, closed) or backtrack(i + 1, opened, closed + 1)

                return memo[state]

        return backtrack(0, 0, 0)