class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        word_dict = {
            2: ("a","b","c") ,
            3: ("d","e","f") ,
            4: ("h","g","i") ,
            5: ("j","k","l") ,
            6: ("m","n","o") ,
            7: ("p","q","r", "s") ,
            8: ("t","u","v") ,
            9: ("w","x","y", "z")
        }

        def backtrack(idx, curr):
            if idx == len(digits):
                res.append(curr)
            else:
                num = int(digits[idx])

                for c in word_dict[num]:
                    backtrack(idx + 1, curr + c)
        

        backtrack(0, '')

        return res