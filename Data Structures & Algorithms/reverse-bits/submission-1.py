class Solution:
    def reverseBits(self, n: int) -> int:
        res = ''

        for i in range(31, -1, -1):
            res = res + str((n >> 31 - i) & 1)
        
        return int(res, 2)