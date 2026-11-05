class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        len_longest = 0

        for i in range(len(s)):
            # Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l + 1) > len_longest:
                longest = s[l + 1:r]
                len_longest = r - l + 1
            
            # Even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if (r - l + 1) > len_longest:
                longest = s[l + 1:r]
                len_longest = r - l + 1
        
        return longest