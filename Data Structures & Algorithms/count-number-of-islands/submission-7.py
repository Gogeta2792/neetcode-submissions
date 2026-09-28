class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            directions = ((0,1), (0,-1), (1,0), (-1,0))

            for dir_r, dir_c in directions:
                new_r = dir_r + r
                new_c = dir_c + c

                if 0 <= new_r < rows and \
                0 <= new_c < cols and \
                grid[new_r][new_c] == "1":
                    grid[new_r][new_c] = "0"
                    dfs(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands