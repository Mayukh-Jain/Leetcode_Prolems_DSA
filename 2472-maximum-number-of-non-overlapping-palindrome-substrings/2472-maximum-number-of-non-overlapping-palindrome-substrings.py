class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i <= n - k:
            sub_k = s[i : i + k]
            if sub_k == sub_k[::-1]:
                ans += 1
                i += k
                continue
            
            if i + k + 1 <= n:
                sub_k1 = s[i : i + k + 1]
                if sub_k1 == sub_k1[::-1]:
                    ans += 1
                    i += k + 1
                    continue
            
            i += 1
            
        return ans