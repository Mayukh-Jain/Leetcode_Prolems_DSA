class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=0
        b=0
        for i in str(n):
            if i=="0":
                continue
            a=a*10+int(i)
            b+=int(i)
        return(a*b)