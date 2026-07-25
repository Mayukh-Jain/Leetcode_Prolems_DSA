class Solution:
    def numSteps(self, s: str) -> int:
        st=0
        carry=0
        for i in range(len(s)-1,0,-1):
            val=int(s[i])+carry
            if val==1:
                st+=2
                carry=1
            else:
                st+=1

        return st+carry