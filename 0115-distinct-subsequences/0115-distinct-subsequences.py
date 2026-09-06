class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        dp=[1]+[0]*m

        for ch in s:
            for j in range(m,0,-1):
                if ch==t[j-1]:
                    dp[j]+=dp[j-1]
        return dp[m]
        
        # n,m=len(s),len(t)
        # dp=[[0]*(m+1) for i in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=1

        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if s[i-1]==t[j-1]:
        #             dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j]
        
        # return dp[n][m]

        # def solve(i,j):
        #     if j==0: return 1
        #     if i==0: return 0

        #     if s[i-1]==t[j-1]: 
        #         return solve(i-1,j-1)+solve(i-1,j)
        #     else:
        #         return solve(i-1,j)
        # return solve(len(s),len(t))