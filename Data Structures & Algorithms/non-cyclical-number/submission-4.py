class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while n != 1:
            hashset.add(n)

            string = str(n)
            new = 0
            for c in string:
                new += int(c) ** 2

            n = new

            if n in hashset:
                return False
        
        return True