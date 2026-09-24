class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        def ds(n):
            res=0
            while n>0:
                res+=n%10
                n//=10
            return res
        for i in range(n):
            if i==ds(nums[i]): return i
        return -1
