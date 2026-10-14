class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        biggest = 0

        def dfs(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == 0:
                return 0
            
            size = 1
            grid[r][c] = 0

            size += dfs(r + 1, c)
            size += dfs(r - 1, c)
            size += dfs(r, c + 1)
            size += dfs(r, c - 1)

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    biggest = max(biggest, dfs(r,c))
        
        return biggest