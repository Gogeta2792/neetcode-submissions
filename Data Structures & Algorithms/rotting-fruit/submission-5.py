class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        minutes, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        
        while q and fresh:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dir_r, dir_c in directions:
                    new_r = row + dir_r
                    new_c = col + dir_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        q.append((new_r,new_c))
                        fresh -= 1
            minutes += 1

        return -1 if fresh else minutes