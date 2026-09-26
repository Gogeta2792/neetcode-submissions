class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        freq = defaultdict(int)
        longest = 0

        while right < len(s):
            freq[s[right]] += 1

            if not (right - left + 1) - max(freq.values()) <= k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1

        return longest