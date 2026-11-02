class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while (mask & b):
            a, b = a ^ b, (a & b) << 1
        
        return a if b == 0 else mask & a