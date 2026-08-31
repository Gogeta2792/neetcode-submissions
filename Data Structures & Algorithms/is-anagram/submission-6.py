class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l, r = 0, len(s) - 1
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count