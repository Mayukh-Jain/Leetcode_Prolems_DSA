from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        m=defaultdict(int)
        left=0   
        res=0

        for right in range(len(nums)):
            m[nums[right]]+=1

            while m[nums[right]]>k:
                m[nums[left]]-=1
                left+=1
            
            res=max(res,right-left+1)
        
        return res