class Solution:
    def checkString(self, s: str) -> bool:
        b=False
        for ch in s: 
            if ch=='a' and b:
                return False
            if ch=='b': b=True
        return True