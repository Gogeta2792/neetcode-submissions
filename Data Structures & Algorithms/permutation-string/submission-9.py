class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        cnt_1 = Counter(s1)
        cnt_2 = Counter(s2[l:r])

        while r < len(s2):
            if cnt_1 == cnt_2:
                return True
            else:
                cnt_2[s2[l]] -= 1
                cnt_2[s2[r]] += 1
                l += 1
                r += 1
        
        return cnt_1 == cnt_2