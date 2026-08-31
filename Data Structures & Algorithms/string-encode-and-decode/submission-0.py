class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        length = ""
        while i < len(s):
            if s[i].isdigit():
                length += s[i]
                i += 1
            elif s[i] == '#':
                #Then we know that int(length) is the length of the encoded string
                i += 1
                decoded_strs.append(s[i: i + int(length)])
                i += int(length)
                length = ""
            else:
                return decoded_strs

        return decoded_strs

"""
#Naive approach
["Hello","World"] -> "HelloWorld" -> I would know to seperate this by using the upper case letters, but this breaks for
["hello","world"]

So we would have to mark where each word begins #Not space between words since it would break for
["hello","wor ld"]
So something like
["Hello","World"] -> "#Hello#World"
But that breaks with
["hello","world","number#5"]

Hence, I will append a prefix to each word before concatenating into one string
"""

