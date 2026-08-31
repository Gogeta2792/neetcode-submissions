class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }

        for bracket in s:
            if bracket in bracket_map.keys(): #if opening
                stack.append(bracket)
            else: #if closing
                if not stack:
                    return False
                if bracket != bracket_map[stack.pop()]:
                    return False
        
        if stack:
            return False
        else:
            return True