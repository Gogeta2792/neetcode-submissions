class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        l, r = 0, 0

        while l < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            decoded_strings.append(s[r + 1: r + length + 1])
            l = r + length + 1
            r = l

        return decoded_strings