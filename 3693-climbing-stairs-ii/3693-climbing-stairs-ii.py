class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        @cache
        def get_min_cost(step: int) -> int:
            if step == 0:
                return 0
            
            current_step_cost = costs[step - 1]
            min_cost = float('inf')
            
            if step >= 1:
                min_cost = min(min_cost, get_min_cost(step - 1) + current_step_cost + 1)
            if step >= 2:
                min_cost = min(min_cost, get_min_cost(step - 2) + current_step_cost + 4)
            if step >= 3:
                min_cost = min(min_cost, get_min_cost(step - 3) + current_step_cost + 9)
                
            return min_cost
            
        return get_min_cost(n)