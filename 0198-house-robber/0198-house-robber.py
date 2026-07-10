class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        
        for money in nums:
            curr=max(prev1,money+prev2)
            prev2=prev1
            prev1=curr
        
        return prev1