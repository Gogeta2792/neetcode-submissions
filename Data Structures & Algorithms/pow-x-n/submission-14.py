class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            
            else:
                res = helper(x, n // 2)
                res *= res

                if n % 2:
                    res *= x

                return res

        return helper(x, n) if n >= 0 else 1/helper(x, -n)