class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        for c in magazine:
            freq[c]=freq.get(c,0)+1
        for i in ransomNote:
            if i in freq and freq[i]>0:
                freq[i]-=1
            else:
                return False
        return True