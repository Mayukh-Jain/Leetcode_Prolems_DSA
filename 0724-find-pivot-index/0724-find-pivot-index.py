class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        a=0
        for i in range(len(nums)):
            if s-a-nums[i]==a:
                return i
            a+=nums[i]
        return -1