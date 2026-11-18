import math

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)
                
        cost = [[math.inf] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = math.inf
                
                for d in divisors[L]:
                    changes = 0
                    
                    for start in range(d):
                        left = i + start
                        right = i + start + ((L - 1 - start) // d) * d
                        
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                            
                    if changes < min_changes:
                        min_changes = changes
                        
                cost[i][j] = min_changes
                
        dp = [[math.inf] * (k + 1) for _ in range(n)]
        
        for i in range(1, n):
            dp[i][1] = cost[0][i]
            
        for p in range(2, k + 1):
            for i in range(p * 2 - 1, n):
                for j in range((p - 1) * 2 - 1, i - 1):
                    if dp[j][p - 1] != math.inf and cost[j + 1][i] != math.inf:
                        dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j + 1][i])
                        
        return dp[n - 1][k]