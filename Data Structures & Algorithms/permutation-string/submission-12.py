class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        cnt_1 = Counter(s1)
        cnt_2 = Counter(s2[:len1])

        l, r = 0, len1 - 1

        while r < len2 - 1:
            if cnt_1 == cnt_2:
                return True
            else:
                cnt_2[s2[l]] -= 1
                l += 1
                r += 1
                cnt_2[s2[r]] += 1
        
        return cnt_1 == cnt_2