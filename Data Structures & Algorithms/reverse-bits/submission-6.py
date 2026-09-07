class Solution:
    def reverseBits(self, n: int) -> int:
        string = f"{n:032b}"
        string = string[::-1]

        return int(string,2)