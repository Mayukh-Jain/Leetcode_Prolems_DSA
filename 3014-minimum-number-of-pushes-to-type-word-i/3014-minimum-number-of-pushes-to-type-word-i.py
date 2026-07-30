class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(set(word))
        res=0
        m=1
        while n>0:
            take=min(n,8)
            res+=take*m
            n-=8
            m+=1
        return res