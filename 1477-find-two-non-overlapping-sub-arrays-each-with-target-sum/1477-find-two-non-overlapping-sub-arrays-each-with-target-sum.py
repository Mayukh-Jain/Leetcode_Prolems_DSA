class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        curr_sum = 0
        l = 0
        ans = float('inf')
        best_so_far = float('inf')
        
        for r in range(n):
            curr_sum += arr[r]
            
            while curr_sum > target and l <= r:
                curr_sum -= arr[l]
                l += 1
                
            if curr_sum == target:
                curr_len = r - l + 1
                
                if l > 0 and min_len[l - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[l - 1])
                
                best_so_far = min(best_so_far, curr_len)
            
            min_len[r] = best_so_far
            
        return ans if ans != float('inf') else -1