class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for b in s:
            if b=="(" or b=="[" or b=="{":
                stack.append(b)
            elif not stack or (b == ")" and stack[-1] != "(") or (b == "}" and stack[-1] != "{") or (b == "]" and stack[-1] != "["):
                return False
            else:
                stack.pop()
        return not stack