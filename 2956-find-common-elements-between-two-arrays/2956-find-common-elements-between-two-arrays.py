class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        a1=sum(1 for num in nums1 if num in s2)
        a2=sum(1 for num in nums2 if num in s1)
        return [a1,a2]

        # nums1.sort()
        # nums2.sort()
        # m=len(nums1)
        # n=len(nums2)
        # res=[0,0]
        # for i in range(m):
        #     if nums1[i] in nums2:
        #         res[0]+=1
        # for i in range(n):
        #     if nums2[i] in nums1:
        #         res[1]+=1
        # return res