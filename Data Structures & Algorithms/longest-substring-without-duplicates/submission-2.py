class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest_substring = 0, 0
        letter_set = set()

        for right in range(len(s)):
            while s[right] in letter_set:
                letter_set.remove(s[left])
                left += 1
            letter_set.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring