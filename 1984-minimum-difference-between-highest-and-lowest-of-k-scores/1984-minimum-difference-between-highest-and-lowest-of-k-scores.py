class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1 or k==1: return 0

        nums.sort()
        res=float('inf')

        for i in range(n-k+1):
            res=min(res,nums[i+k-1]-nums[i])
        
        return int(res)