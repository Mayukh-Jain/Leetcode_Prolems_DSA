from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def maxScoreDiff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            
            pick_left = nums[i] - maxScoreDiff(i + 1, j)
            
            pick_right = nums[j] - maxScoreDiff(i, j - 1)
            
            return max(pick_left, pick_right)
        
        return maxScoreDiff(0, len(nums) - 1) >= 0