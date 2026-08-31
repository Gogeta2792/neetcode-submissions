class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = {}
        for letter in s:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        for letter in t:
            if letter in dictionary:
                dictionary[letter] -= 1
            else:
                return False
        
        return all(letter_count == 0 for letter_count in dictionary.values())