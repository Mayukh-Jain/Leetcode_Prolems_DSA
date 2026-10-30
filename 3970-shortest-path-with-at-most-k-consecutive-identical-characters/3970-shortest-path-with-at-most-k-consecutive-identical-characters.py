import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        pq = [(0, 0, 1)]
        
        min_count = [float('inf')] * n
        
        while pq:
            w, u, c = heapq.heappop(pq)
            
            if u == n - 1:
                return w
                
            if c >= min_count[u]:
                continue
            
            min_count[u] = c
            
            for v, edge_w in adj[u]:
                if labels[u] == labels[v]:
                    new_c = c + 1
                else:
                    new_c = 1
                
                if new_c <= k:
                    heapq.heappush(pq, (w + edge_w, v, new_c))
                    
        return -1