class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def prod(n):
            p=1
            x=n
            while x>0:
                p*=x%10
                x//=10
            return p
        
        while True:
            if prod(n)%t==0:
                return n
            n+=1