class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        def calculate_cost(x: int) -> int:
            remaining_1 = max(0, need1 - x)
            remaining_2 = max(0, need2 - x)
            return (x * costBoth) + (remaining_1 * cost1) + (remaining_2 * cost2)
        
        return min(
            calculate_cost(0), 
            calculate_cost(need1), 
            calculate_cost(need2)
        )