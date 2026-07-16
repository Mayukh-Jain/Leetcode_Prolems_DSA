class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        curr=0
        flowerbed=[0]+flowerbed+[0]
        for i in flowerbed:
            if i==0:
                curr+=1
            else:
                curr=0
            if curr>2 and curr%2==1:
                count+=1
        return count>=n