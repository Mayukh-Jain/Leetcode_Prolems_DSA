class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for c in s:
            m[c]=m.get(c,0)+1
        for i,c in enumerate(s):
            if m[c]==1:
                return i
        return -1