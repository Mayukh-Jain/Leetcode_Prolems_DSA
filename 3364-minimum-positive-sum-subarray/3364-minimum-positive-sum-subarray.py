class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_pos_sum = float('inf')
        n = len(nums)
        
        for length in range(l, r + 1):
            window_sum = sum(nums[:length])
            if window_sum > 0:
                min_pos_sum = min(min_pos_sum, window_sum)
                
            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                if window_sum > 0:
                    min_pos_sum = min(min_pos_sum, window_sum)
                    
        return min_pos_sum if min_pos_sum != float('inf') else -1