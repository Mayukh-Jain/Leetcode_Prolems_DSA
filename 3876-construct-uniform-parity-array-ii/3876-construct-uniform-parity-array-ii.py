class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1)%2==1: return True
        return all(n%2==0 for n in nums1)