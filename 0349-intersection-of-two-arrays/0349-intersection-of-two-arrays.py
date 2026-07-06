class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=len(nums1)
        n=len(nums2)
        i,j=0,0
        nums1.sort()
        nums2.sort()
        res=[]
        while i<m and j<n:
            if i>0 and nums1[i]==nums1[i-1]:
                i+=1
                continue
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                j+=1
                i+=1
        return res