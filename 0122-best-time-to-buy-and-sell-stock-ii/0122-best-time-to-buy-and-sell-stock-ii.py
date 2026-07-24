class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        currmin=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>currmin:
                res+=prices[i]-currmin
            currmin=prices[i]
        return res