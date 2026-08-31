class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        q = collections.deque()

        def bfs(r,c):
            size = 1
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for d_r, d_c in directions:
                    new_r = row + d_r
                    new_c = col + d_c
                    if (0 <= new_r < rows and
                        0 <= new_c < cols and
                        grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 0
                        q.append((new_r, new_c))
                        size += 1
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area, bfs(r,c))
        
        return max_area