from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        pref_val = [0] * (n + 1)
        pref_sum = [0] * (n + 1)
        pref_count = [0] * (n + 1)
        
        for i in range(n):
            val = int(s[i])
            if val != 0:
                pref_val[i+1] = (pref_val[i] * 10 + val) % MOD
                pref_sum[i+1] = pref_sum[i] + val
                pref_count[i+1] = pref_count[i] + 1
            else:
                pref_val[i+1] = pref_val[i]
                pref_sum[i+1] = pref_sum[i]
                pref_count[i+1] = pref_count[i]
                
        res = []
        for L, R in queries:
            R += 1 
            
            count = pref_count[R] - pref_count[L]
            
            digit_sum = pref_sum[R] - pref_sum[L]
            
            concat_val = (pref_val[R] - pref_val[L] * pow10[count]) % MOD
            
            answer = (concat_val * digit_sum) % MOD
            res.append(answer)
            
        return res