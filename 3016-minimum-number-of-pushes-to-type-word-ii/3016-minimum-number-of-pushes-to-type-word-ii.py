class Solution:
    def minimumPushes(self, word: str) -> int:
        m={}
        for ch in word:
            m[ch]=m.get(ch,0)+1
        freq=sorted(m.values(),reverse=True)
        res=0
        for i,f in enumerate(freq):
            res+=f*(i//8+1)
        return res