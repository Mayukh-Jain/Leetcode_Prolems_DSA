class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True) + [0]
        k = k1 + k2
        
        if sum(diffs) <= k: 
            return 0
            
        for i, (curr, nxt) in enumerate(zip(diffs, diffs[1:])):
            count = i + 1
            reduction = (curr - nxt) * count
            
            if k >= reduction:
                k -= reduction
            else:
                q, r = divmod(k, count)
                return (count - r) * (curr - q)**2 + r * (curr - q - 1)**2 + sum(x**2 for x in diffs[i+1:])
                
        return 0