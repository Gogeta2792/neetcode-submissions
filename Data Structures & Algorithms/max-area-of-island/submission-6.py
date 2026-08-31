class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        stack = []
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(r,c):
            count = 1
            stack.append((r,c))
            while stack:
                row, col = stack.pop()
                for dir_r, dir_c in directions:
                    new_r = row + dir_r
                    new_c = col + dir_c
                    if (0 <= new_r < rows and
                        0 <= new_c < cols and
                        grid[new_r][new_c] == 1):
                        count += 1
                        grid[new_r][new_c] = 0
                        stack.append((new_r, new_c))
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area, dfs(r,c))
        
        return max_area