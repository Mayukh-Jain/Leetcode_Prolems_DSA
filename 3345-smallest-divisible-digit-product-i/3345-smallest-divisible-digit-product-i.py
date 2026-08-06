class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def prod(n):
            p=1
            for num in str(n):
                p*=int(num)
            return p
        
        while True:
            if prod(n)%t==0:
                return n
            n+=1