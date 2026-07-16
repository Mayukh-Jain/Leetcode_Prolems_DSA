class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        half=(n1+n2)//2
        if n2<n1:
            nums1,nums2=nums2,nums1
            n1,n2=n2,n1
        l,r=0,n1
        while True:
            i=(l+r)//2
            j=half-i

            l1=nums1[i-1] if i > 0 else float('-infinity')
            r1=nums1[i] if i<n1 else float('infinity')
            l2=nums2[j-1] if j > 0 else float('-infinity')
            r2=nums2[j] if j<n2 else float('infinity')

            if l1<=r2 and  l2<=r1:
                if (n1+n2)%2:
                    return float(min(r1,r2))
                else:
                    return (max(l1,l2)+min(r1,r2))/2.0
            elif  l1>r2:
                r=i-1
            else:
                l=i+1