from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def f(i,t):
            if t==0: return 0
            if i<0: return float('inf')

            nt=f(i-1,t)
            take=float('inf')
            if coins[i]<=t:
                take=1+f(i,t-coins[i])
            return min(nt,take)
        res=f(len(coins)-1,amount)
        return res if res!=float('inf') else -1