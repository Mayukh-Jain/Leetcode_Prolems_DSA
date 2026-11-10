class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ts=sum(nums)
        if ts%2==1: return False
        t=ts//2

        @cache
        def ss(n,t):
            if t==0: return True
            if n==0: return False
            if nums[n-1]>t: return ss(n-1,t)
            return ss(n-1,t) or ss(n-1,t-nums[n-1])

        return ss(len(nums),t)