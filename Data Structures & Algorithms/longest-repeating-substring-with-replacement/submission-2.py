class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left, right = 0, 0
        longest = 0

        while right < len(s):
            freq[s[right]] += 1

            while (right - left + 1) - max(freq.values()) > k: #invalid
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        
        return longest