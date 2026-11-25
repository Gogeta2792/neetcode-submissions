class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt_1 = Counter(s)
        cnt_2 = Counter(t)
        
        return cnt_1 == cnt_2