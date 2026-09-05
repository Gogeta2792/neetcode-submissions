class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(x, y):
            if (x,y) in memo:
                return memo[(x,y)]
            if x == m - 1 or y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            memo[(x,y)] = (helper(x + 1, y) if x < m - 1 else 0) + (helper(x, y + 1) if y < n - 1 else 0)
            return memo[(x,y)]

        
        return helper(0,0)