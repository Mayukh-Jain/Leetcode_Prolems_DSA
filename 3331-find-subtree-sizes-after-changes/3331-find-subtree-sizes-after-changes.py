class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        sys.setrecursionlimit(max(2000, n + 500))
        
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        ans = [1] * n
        last_seen = [-1] * 26
        
        def dfs(u: int):
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            
            last_seen[char_idx] = u
            
            for v in adj[u]:
                dfs(v)
                
            last_seen[char_idx] = prev_ancestor
            
            if u != 0:
                new_p = prev_ancestor if prev_ancestor != -1 else parent[u]
                ans[new_p] += ans[u]
                
        dfs(0)
        return ans