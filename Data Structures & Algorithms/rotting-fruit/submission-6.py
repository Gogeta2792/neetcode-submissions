class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, minutes = 0, 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = ((0,-1), (0,1), (-1,0), (1,0))

        while q and fresh:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dir_r, dir_c in directions:
                    new_r = dir_r + r
                    new_c = dir_c + c

                    if 0 <= new_r < rows and \
                       0 <= new_c < cols and \
                       grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
        
        return minutes if not fresh else -1