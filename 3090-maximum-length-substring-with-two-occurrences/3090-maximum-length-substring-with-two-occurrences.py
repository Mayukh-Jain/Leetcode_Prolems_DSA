class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m={}
        l=0
        res=0
        for r in range(len(s)):
            m[s[r]]=m.get(s[r],0)+1
            while m[s[r]]>2:
                m[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res