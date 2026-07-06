class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m=len(nums1)
        n=len(nums2)
        res=[0,0]
        for i in range(m):
            if nums1[i] in nums2:
                res[0]+=1
        for i in range(n):
            if nums2[i] in nums1:
                res[1]+=1
        return res