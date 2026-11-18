class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        l, r = 0, len(s1)

        cnt_1, cnt_2 = [0] * 26, [0] * 26 

        for i in range(len(s1)):
            cnt_1[ord(s1[i]) - ord('a')] += 1
            cnt_2[ord(s2[i]) - ord('a')] += 1

        while r < len(s2):
            if cnt_1 == cnt_2:
                return True
            else:
                cnt_2[ord(s2[l]) - ord('a')] -= 1
                cnt_2[ord(s2[r]) - ord('a')] += 1
                l += 1
                r += 1
        
        return cnt_1 == cnt_2