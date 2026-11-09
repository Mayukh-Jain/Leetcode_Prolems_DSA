from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        
        busy = []
        
        counts = [0] * k
        
        for i, (arr_time, process_time) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            
            if not available:
                continue
            
            target = i % k
            idx = available.bisect_left(target)
            
            if idx == len(available):
                idx = 0
                
            assigned_server = available[idx]
            
            available.remove(assigned_server)
            counts[assigned_server] += 1
            heapq.heappush(busy, (arr_time + process_time, assigned_server))
            
        max_requests = max(counts)
        return [i for i, count in enumerate(counts) if count == max_requests]