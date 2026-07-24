class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        p = 2 
        
        for i in range(2, len(nums)):
           if nums[i] != nums[p - 2]:
                nums[p] = nums[i]
                p += 1
                
        return p