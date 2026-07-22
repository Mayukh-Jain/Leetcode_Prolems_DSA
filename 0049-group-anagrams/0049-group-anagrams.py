class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for s in strs:
            k="".join(sorted(s))
            if k not in m:
                m[k]=[]
            m[k].append(s)
        return list(m.values())