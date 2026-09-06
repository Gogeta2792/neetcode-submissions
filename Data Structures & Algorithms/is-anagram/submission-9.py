class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = Counter(s)
        hash_t = Counter(t)

        return hash_s == hash_t