class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumEven=0
        for i in range(2,n*2+1,2):
            sumEven+=i
        for i in range(1,n*2,2):
            sumOdd+=i
        while sumOdd:
            sumEven,sumOdd=sumOdd,sumEven%sumOdd
        return sumEven