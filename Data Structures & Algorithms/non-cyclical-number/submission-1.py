class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n > 1:
            seen.add(n)
            digits = str(n)
            n = sum(int(c) ** 2 for c in digits)
            if n in seen:
                return False

        return True