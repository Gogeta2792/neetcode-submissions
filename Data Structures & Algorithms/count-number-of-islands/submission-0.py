class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        #seen_islands = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        def dfs(row, col):
            grid[row][col] = '0'
            for dir_row, dir_col in directions:
                new_row = dir_row + row
                new_col = dir_col + col
                #if this is inside of the grid
                #check if it is '1' & add it to seen_islands
                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] == '1'):
                    dfs(new_row, new_col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
                else: #0
                    continue
        
        return islands



#if it's 0, do nothing
#if it's 1
    #is it part of an existing island?
        #if so, do nothing
    #if it is not part of an existing island
        #increment the number of islands
        #find the WHOLE island