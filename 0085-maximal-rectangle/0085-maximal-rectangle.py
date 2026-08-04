class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        heights = [0] * c
        res = 0

        for row in matrix:
            for j in range(c):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            res = max(res, self.lh(heights))

        return res
        
    def lh(self, arr):
        ma=0
        stack=[]
        arr.append(0)
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                he=arr[stack.pop()]
                w=i if not stack else i-stack[-1]-1
                ma=max(ma,he*w)
            stack.append(i)
        return ma
