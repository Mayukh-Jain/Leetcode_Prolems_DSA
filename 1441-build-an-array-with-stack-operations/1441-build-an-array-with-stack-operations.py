class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        target=set(target)
        for i in range(1,min(1+n,max(target)+1)):
            if i in target:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
        return res