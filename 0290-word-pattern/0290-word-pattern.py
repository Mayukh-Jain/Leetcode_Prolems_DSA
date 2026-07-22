class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=[pattern.index(t) for t in pattern]
        s=s.split()
        b=[s.index(t) for t in s]

        return a==b