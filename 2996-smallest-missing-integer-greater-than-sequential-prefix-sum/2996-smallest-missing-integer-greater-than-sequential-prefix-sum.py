class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curr+=nums[i]
            else:
                break
        s=set(nums)
        while True:
            if curr in s:
                curr+=1
            else:
                break
        return curr