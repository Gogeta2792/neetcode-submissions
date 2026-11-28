class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []

        l, r = 0, 0

        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r += length + 1
            decoded_strings.append(s[l:r])
            
            l = r
        
        return decoded_strings