class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = {}
        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1
        
        for letter in t:
            if letter not in s_letters:
                return False
            s_letters[letter] -= 1
        
        return (all(value == 0 for value in s_letters.values()))
        