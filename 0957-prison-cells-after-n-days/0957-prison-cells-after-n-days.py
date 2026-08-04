class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nextState(arr):
            c=[0]*8
            for i in range(1,7):
                c[i]=1 if arr[i-1]==arr[i+1] else 0
            return c

        cells=nextState(cells)
        n-=1
        n%=14
        for _ in range(n):
            cells=nextState(cells)
        return cells