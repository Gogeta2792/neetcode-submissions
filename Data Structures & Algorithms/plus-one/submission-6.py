class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in range(len(digits) - 1, -1 , -1):
            if digits[i] <= 9:
                break
            if i == 0 and digits[i] > 9:
                return [1] + [0] * len(digits)
            else:
                digits[i] = 0
                digits[i-1] += 1

        return digits