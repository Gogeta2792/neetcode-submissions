class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                if i == 0:
                    res = [0] * (len(digits) + 1)
                    res[0] = 1
                    return res
                else:
                    digits[i] = 0
                    digits[i-1] += 1
        
        return digits