class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            # Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l + 1: r]) > len(longest):
                longest = s[l + 1: r]
            
            # Even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l + 1: r]) > len(longest):
                longest = s[l + 1: r]
        
        return longest