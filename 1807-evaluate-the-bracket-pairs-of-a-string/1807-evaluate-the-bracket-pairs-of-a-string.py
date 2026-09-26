class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kd={k:v for k,v in knowledge}
        res=[]
        n=len(s)
        i=0
        while i<n:
            curr=''
            if s[i]=="(":
                i+=1
                while s[i]!=")":
                    curr+=s[i]
                    i+=1
                i+=1
                # print(curr)
                if curr in kd:
                    res.append(kd[curr])
                else:  res.append('?')
            else:
                res.append(s[i])
                i+=1
        return "".join(res)