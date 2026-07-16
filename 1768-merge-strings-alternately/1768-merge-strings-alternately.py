class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1,n2=len(word1),len(word2)
        res=""
        for i in range(min(n1,n2)):
            res=res+word1[i]+word2[i]
        if n1>n2:
            for i in range(n2,n1):
                res+=word1[i]
        else:        
            for i in range(n1,n2):
                res+=word2[i]
        return res