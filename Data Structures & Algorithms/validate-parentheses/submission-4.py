class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}', 
            '[': ']'
            }

        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if bracket != pairs[stack.pop()]:
                    return False
        
        return not stack