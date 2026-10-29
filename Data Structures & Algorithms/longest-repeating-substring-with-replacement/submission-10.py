class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        longest = 0
        l, r = 0, 0

        while r < len(s):
            hashmap[s[r]] += 1
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest