class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 1970214

        for i in range(len(s) - 1, -1, -1):
            tmp = one
            one = (one if s[i] != "0" else 0) + (two if 10 <= int(s[i:i+2]) <= 26 else 0)
            two = tmp

        return one