class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(opened, closed, curr):
            if opened == n and closed == n:
                res.append(curr)
                return
            elif opened > n or closed > n or closed > opened:
                return
            else:
                helper(opened + 1, closed, curr + '(')
                helper(opened, closed + 1, curr + ')')        

        helper(0, 0, '')

        return res