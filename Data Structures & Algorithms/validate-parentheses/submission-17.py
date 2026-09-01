class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if bracket_map[bracket] != stack.pop():
                    return False
        
        return not stack