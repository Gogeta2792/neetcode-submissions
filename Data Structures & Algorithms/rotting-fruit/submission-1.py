class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh, minutes = 0, 0

        if not grid or not grid[0]:
            return -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q and fresh:
            minutes += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dir_r, dir_c in directions:
                    new_row = r + dir_r
                    new_col = c + dir_c
                    if (0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        q.append((new_row, new_col))
        
        if fresh:
            return -1
        else:
            return minutes