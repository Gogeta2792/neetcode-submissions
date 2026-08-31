class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        bracket_map = {']' : '[',
                        ')' : '(',
                        '}' : '{'}
        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            else: #closing brackets
                if not stack or bracket_map[bracket] != stack.pop():
                    return False
        return not stack