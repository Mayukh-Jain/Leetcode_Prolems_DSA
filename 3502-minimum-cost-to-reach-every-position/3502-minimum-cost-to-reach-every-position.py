class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res=[]
        res.append(cost[0])
        for i in cost[1:]:
            if i<res[-1]:
                res.append(i)
            else:
                res.append(res[-1])
        return res