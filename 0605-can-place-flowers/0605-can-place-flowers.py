class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # count=0
        # curr=0
        # flowerbed=[0]+flowerbed+[0]
        # for i in flowerbed:
        #     if i==0:
        #         curr+=1
        #     else:
        #         curr=0
        #     if curr>2 and curr%2==1:
        #         count+=1
        # return count>=n

        if n == 0:
            return True
            
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i]=1
                    n -= 1            
                    if n == 0:
                        return True
                        
        return n <= 0