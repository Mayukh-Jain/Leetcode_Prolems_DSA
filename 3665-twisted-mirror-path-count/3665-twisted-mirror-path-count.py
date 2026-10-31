from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        jump_r0 = [[-1] * n for _ in range(m)]
        jump_c0 = [[-1] * n for _ in range(m)]
        jump_r1 = [[-1] * n for _ in range(m)]
        jump_c1 = [[-1] * n for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    jump_r0[r][c] = jump_r1[r][c] = r
                    jump_c0[r][c] = jump_c1[r][c] = c
                    continue

                if grid[r][c] == 0:
                    jump_r0[r][c] = jump_r1[r][c] = r
                    jump_c0[r][c] = jump_c1[r][c] = c
                else:
                    if r + 1 < m:
                        jump_r0[r][c] = jump_r1[r + 1][c]
                        jump_c0[r][c] = jump_c1[r + 1][c]
                    
                    if c + 1 < n:
                        jump_r1[r][c] = jump_r0[r][c + 1]
                        jump_c1[r][c] = jump_c0[r][c + 1]

        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue

                if grid[r][c] == 0 or (r == 0 and c == 0):
                    paths = 0
                    
                    if c + 1 < n:
                        nr = jump_r0[r][c + 1]
                        nc = jump_c0[r][c + 1]
                        if nr != -1:
                            paths = (paths + dp[nr][nc]) % MOD
                            
                    if r + 1 < m:
                        nr = jump_r1[r + 1][c]
                        nc = jump_c1[r + 1][c]
                        if nr != -1:
                            paths = (paths + dp[nr][nc]) % MOD
                            
                    dp[r][c] = paths

        return dp[0][0]