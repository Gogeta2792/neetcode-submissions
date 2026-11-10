class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        hashset = set()

        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest