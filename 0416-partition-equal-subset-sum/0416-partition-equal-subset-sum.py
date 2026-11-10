class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ts=sum(nums)
        if ts%2==1: return False
        t=ts//2

        # @cache
        # def ss(n,t):
        #     if t==0: return True
        #     if n==0: return False
        #     if nums[n-1]>t: return ss(n-1,t)
        #     return ss(n-1,t) or ss(n-1,t-nums[n-1])

        # return ss(len(nums),t)

        n=len(nums)
        dp=[[False]*(t+1) for _ in range(n+1)]

        for i in range(n+1): dp[i][0]=True

        for i in range(1,n+1):
            for j in range(1,t+1):
                if nums[i-1]>j: dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
        
        return dp[n][t]