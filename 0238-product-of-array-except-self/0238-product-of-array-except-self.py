class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n
        p=1
        for i in range(n):
            res[i]=p
            p*=nums[i]
        s=1
        for i in range(n-1,-1,-1):
            res[i]*=s
            s*=nums[i]
        return res