class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        freqmap = defaultdict(int)

        while r < len(s):
            freqmap[s[r]] += 1

            while r - l + 1 - max(freqmap.values()) > k:
                freqmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
            
        return longest