class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def bfs(r,c):
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dir_r, dir_c in directions:
                    new_r = dir_r + row
                    new_c = dir_c + col
                    if (0 <= new_r < rows and
                        0 <= new_c < cols and
                        grid[new_r][new_c] == '1'):
                        grid[new_r][new_c] = '0'
                        q.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    grid[r][c] = "0"
                    bfs(r,c)
        
        return island_count