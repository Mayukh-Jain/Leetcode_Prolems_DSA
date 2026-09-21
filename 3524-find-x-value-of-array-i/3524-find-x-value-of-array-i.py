from typing import List
from collections import defaultdict

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        
        dp = defaultdict(int)

        for num in nums:
            new_dp = defaultdict(int)
            
            new_dp[num % k] += 1
            
            for val, count in dp.items():
                new_dp[(val * num) % k] += count

            for val, count in new_dp.items():
                result[val] += count

            dp = new_dp

        return result