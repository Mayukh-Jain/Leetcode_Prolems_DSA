class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        valid_islands_count = 0
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            current_val = grid[r][c]
            grid[r][c] = 0 
            
            current_val += dfs(r + 1, c)
            current_val += dfs(r - 1, c)
            current_val += dfs(r, c + 1)
            current_val += dfs(r, c - 1)
            
            return current_val

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        valid_islands_count += 1
                        
        return valid_islands_count