class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l, r = 0, 0
        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1

        return longest