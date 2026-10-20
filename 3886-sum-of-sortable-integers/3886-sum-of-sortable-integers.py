class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            is_valid = True
            prev_max = float('-inf')
            for i in range(0, n, k):
                chunk = nums[i:i+k]
                
                c_min = min(chunk)
                c_max = max(chunk)
                
                if c_min < prev_max:
                    is_valid = False
                    break
                drops = sum(1 for j in range(k - 1) if chunk[j] > chunk[j+1])
                if drops > 1 or (drops == 1 and chunk[-1] > chunk[0]):
                    is_valid = False
                    break
                    
                prev_max = c_max
                
            if is_valid:
                total_sum += k
                
        return total_sum