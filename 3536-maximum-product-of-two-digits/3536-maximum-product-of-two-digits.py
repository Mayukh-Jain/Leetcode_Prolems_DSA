class Solution:
    def maxProduct(self, n: int) -> int:
        m1=-1
        m2=-1
        for num in str(n):
            if int(num)>m2:
                m2=int(num)
                if m2>m1:
                    m1,m2=m2,m1
        return m1*m2