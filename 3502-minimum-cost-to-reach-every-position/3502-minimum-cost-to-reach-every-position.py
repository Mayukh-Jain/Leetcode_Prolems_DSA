class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        for i in range(1,len(cost)):
            if cost[i]>cost[i-1]:
                cost[i]=(cost[i-1])
        return cost