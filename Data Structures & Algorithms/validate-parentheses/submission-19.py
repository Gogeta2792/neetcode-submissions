class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for bracket in s:
            if bracket in hashmap.values(): # if open bracket
                stack.append(bracket)
            else: # if close bracket
                if not stack:
                    return False
                else:
                    if not hashmap[bracket] == stack.pop():
                        return False
        
        return not stack