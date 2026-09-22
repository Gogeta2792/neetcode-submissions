class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : ('a', 'b', 'c'),
            '3' : ('d', 'e', 'f'),
            '4' : ('g', 'h', 'i'),
            '5' : ('j', 'k', 'l'),
            '6' : ('m', 'n', 'o'),
            '7' : ('p', 'q', 'r', 's'),
            '8' : ('t', 'u', 'v'),
            '9' : ('w', 'x', 'y', 'z')
        }

        res = []

        if not digits:
            return res

        def helper(idx, word):
            nonlocal res
            if idx == len(digits):
                res = res + [word]
                return word
            
            else:
                for letter in mapping[digits[idx]]:
                    helper(idx + 1, word + letter)
        

        helper(0, '')

        return res