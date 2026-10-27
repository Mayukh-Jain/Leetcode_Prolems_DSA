class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res=["."*n]
        res2=["#"*(n-1)+"."]*(m-1)
        return res+res2