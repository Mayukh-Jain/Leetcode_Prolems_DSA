class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        for idx in range(n):
            total_pushes += (idx // 8) + 1
            
        return total_pushes