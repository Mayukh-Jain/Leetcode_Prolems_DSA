class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            res+=((i+1)*(26-(ord(s[i])-ord('a'))))
        return res