class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])
        
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        active_counts = {}
        left, right = 0, 0
        
        for q, original_index in sorted_queries:
            window_start = q - x
            window_end = q
            
            while right < len(logs) and logs[right][1] <= window_end:
                server_id = logs[right][0]
                active_counts[server_id] = active_counts.get(server_id, 0) + 1
                right += 1
                
            while left < len(logs) and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_counts[server_id] -= 1
                if active_counts[server_id] == 0:
                    del active_counts[server_id]
                left += 1
                
            ans[original_index] = n - len(active_counts)
            
        return ans