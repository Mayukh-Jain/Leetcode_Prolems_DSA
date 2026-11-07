import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        unavailable = []
        
        ans = []
        t = 0
        
        for j in range(len(tasks)):
            t = max(t, j)
            
            if not available:
                t = unavailable[0][0]
                
            while unavailable and unavailable[0][0] <= t:
                free_time, weight, i = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, i))
                
            weight, i = heapq.heappop(available)
            ans.append(i)
            heapq.heappush(unavailable, (t + tasks[j], weight, i))
            
        return ans