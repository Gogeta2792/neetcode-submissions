class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        
        i1, i2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (i1 + i2)

        for i in range(i1):
            for j in range(i2):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        res = res[::-1]
        beg = 0
        for num in res:
            if num != 0:
                break
            beg += 1
        res = res[beg:]

        output = ''
        for c in res:
            output += str(c)
        
        return output