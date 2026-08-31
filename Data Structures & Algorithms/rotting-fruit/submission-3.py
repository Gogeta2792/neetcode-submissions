class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh, minutes = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = ((0,1), (0,-1), (1,0), (-1,0))

        while q and fresh:
            minutes += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dir_r, dir_c in directions:
                    new_row = row + dir_r
                    new_col = col + dir_c
                    if (0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == 1):
                        fresh -= 1
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
        
        return minutes if not fresh else -1