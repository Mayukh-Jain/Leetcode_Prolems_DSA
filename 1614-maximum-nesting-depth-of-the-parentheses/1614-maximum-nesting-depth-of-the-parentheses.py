class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        stack=[]
        for ch in s:
            if ch=='(': stack.append('(')
            elif ch==')': stack.pop()
            res=max(res,len(stack))
        return res