class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        for bracket in s:
            if bracket in hashmap.values():
                stack.append(bracket)
            else:
                if stack:
                    if stack[-1] != hashmap[bracket]:
                        return False
                    stack.pop()
                else:
                    return False
        
        return not stack