class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        counts=[0]*(n+1)
        for c in citations:
            if c>=n:
                counts[n]+=1
            else:
                counts[c]+=1
        
        f=0
        for h in range(n,-1,-1):
            f+=counts[h]
            if f>=h:
                return h
        return 0