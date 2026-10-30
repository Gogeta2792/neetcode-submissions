class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, -696796
        
        for i in range(len(s) - 1, -1, -1):
            one, two = (one if int(s[i:i+1]) != 0 else 0) + (two if 10 <= int(s[i:i+2]) <= 26 else 0), one

        return one