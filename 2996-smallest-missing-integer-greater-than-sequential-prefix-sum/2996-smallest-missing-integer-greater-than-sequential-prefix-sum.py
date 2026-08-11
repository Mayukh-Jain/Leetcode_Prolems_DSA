class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curr+=nums[i]
            else:
                break
        while curr in nums:
            curr+=1
        return curr