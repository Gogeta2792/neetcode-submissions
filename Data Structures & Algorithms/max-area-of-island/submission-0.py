class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        q = collections.deque()
        directions = ((0,1), (0,-1), (1, 0), (-1, 0))
        
        def bfs(row, col):
            size = 1
            q.append((row,col))
            while q:
                r, c = q.popleft()
                for dir_row, dir_col in directions:    
                    new_row, new_col = r + dir_row, c + dir_col
                    if (0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 0
                        size += 1
                        q.append((new_row, new_col))
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area, bfs(r, c))
        return max_area


# Iterate through whole grid
# If we find land, find the size of the entire island
    # Keep track of that number, if it is the biggest so far
    # Say that we've already visited this island