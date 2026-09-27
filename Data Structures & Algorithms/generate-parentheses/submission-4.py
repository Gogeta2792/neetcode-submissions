class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, opens, closes):
            if closes > opens:
                return
            elif opens == n:
                if closes == n:
                    res.append(curr)
                else:
                    backtrack(curr + ')', opens, closes + 1)
            else:
                backtrack(curr + '(', opens + 1, closes)
                backtrack(curr + ')', opens, closes + 1)
        
        backtrack('', 0, 0)

        return res