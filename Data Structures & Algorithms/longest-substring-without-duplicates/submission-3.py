class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        letters = set()

        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest