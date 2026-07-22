class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        if len(t)>n: return ""
        
        freq={}
        for c in t:
            freq[c]=freq.get(c,0)+1
        
        count=len(t)
        wsize=float("inf")
        start_i=0

        i=j=0

        while j<n:
            if s[j] in freq:
                if freq[s[j]] > 0:
                    count -= 1
                freq[s[j]] -= 1
            while (count==0):
                cwsize=j-i+1
                if cwsize<wsize:
                    wsize=cwsize
                    start_i=i 
                if s[i] in freq:
                    freq[s[i]] += 1
                    if freq[s[i]] > 0:
                        count += 1
                i+=1
            j+=1

        return "" if wsize==float("inf") else s[start_i:start_i+wsize]