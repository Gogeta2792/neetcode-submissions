class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def bfs(r,c):
            q.append((r,c))
            curr_area = 1
            while q:
                row, col = q.popleft()
                for dir_r, dir_c in directions:
                    new_r = dir_r + row
                    new_c = dir_c + col
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        q.append((new_r,new_c))
                        curr_area += 1
            return curr_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area, bfs(r,c))
        
        return max_area
