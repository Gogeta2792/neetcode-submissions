class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1
    
        res = 0
        extra_10s = 0
        for bot in range(len(num1) - 1, -1, -1):
            inner_res, inner_10s = 0, 0
            carry = 0

            for top in range(len(num2) - 1, -1, -1):
                curr = int(num1[bot]) * int(num2[top]) + carry
                carry = curr // 10
                inner_res = inner_res + (curr % 10) * 10 ** inner_10s
                inner_10s += 1
            inner_res += carry * 10 ** inner_10s
            res += inner_res * 10 ** extra_10s
            extra_10s += 1
        return str(res)