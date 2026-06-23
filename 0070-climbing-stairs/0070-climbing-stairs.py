class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        o=2
        t=1
        for i in range(3,n+1):
            curr=o+t
            t=o
            o=curr
        return o