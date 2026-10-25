class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            
            grid[r][c] = 1 
            
            top = dfs(r - 1, c)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            return top and bottom and left and right
        
        closed_islands_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        closed_islands_count += 1
                        
        return closed_islands_count