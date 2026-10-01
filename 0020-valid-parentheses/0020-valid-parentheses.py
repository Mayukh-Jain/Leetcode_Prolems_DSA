class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")": "(", "}": "{", "]": "["}

        for b in s:
            if b in m:
                if not stack or stack[-1] != m[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)

        return not stack