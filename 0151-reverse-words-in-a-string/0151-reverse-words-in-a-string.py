class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        arr=s.split()
        return " ".join(arr[::-1])