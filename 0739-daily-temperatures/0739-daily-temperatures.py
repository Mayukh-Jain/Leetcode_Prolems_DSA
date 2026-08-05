class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        stack=[]
        for i,t in enumerate(temperatures[::-1]):
            while stack and stack[-1][1]<=t:
                stack.pop()
            res.append(0 if not stack else i-stack[-1][0])
            stack.append((i,t))
        return res[::-1]