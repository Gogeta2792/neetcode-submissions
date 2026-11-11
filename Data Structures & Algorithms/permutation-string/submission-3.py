class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)

        l, r = 0, len(s1) - 1

        s2_cnt = Counter(s2[l:r + 1])

        while r < len(s2):
            if s1_cnt == s2_cnt:
                return True
            else:
                s2_cnt[s2[l]] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    s2_cnt[s2[r]] += 1
            
        return False