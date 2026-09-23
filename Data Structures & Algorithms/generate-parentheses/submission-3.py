class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(curr, opened, closed):
            if opened == n:
                if closed == n:
                    res.append(curr)
                    return
                else:
                    helper(curr + ")", opened, closed + 1)
            elif closed > opened:
                return
            else:
                helper(curr + "(", opened + 1, closed)
                helper(curr + ")", opened, closed + 1)
        
        helper("", 0, 0)

        return res