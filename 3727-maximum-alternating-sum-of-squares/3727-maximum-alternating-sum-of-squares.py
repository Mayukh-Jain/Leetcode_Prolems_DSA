class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums], reverse=True)
        
        n = len(nums)
        num_positive = (n + 1) // 2 
        
        pos_sum = sum(squares[:num_positive])
        neg_sum = sum(squares[num_positive:])
        
        return pos_sum - neg_sum