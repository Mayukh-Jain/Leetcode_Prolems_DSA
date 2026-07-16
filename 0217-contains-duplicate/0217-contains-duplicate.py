class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        # seen=set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return True
        # return False