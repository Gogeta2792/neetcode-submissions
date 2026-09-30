class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            string = str(n)
            n = sum(int(c) ** 2 for c in string)
            if n in seen:
                return False
            seen.add(n)

        return True