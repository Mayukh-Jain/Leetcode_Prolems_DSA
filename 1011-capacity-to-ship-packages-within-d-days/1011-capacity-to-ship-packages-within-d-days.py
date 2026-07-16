class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        best_capacity = right

        def can_ship(n): #n is capacity
            day=1
            currw=0
            for weight in weights:
                if currw+weight>n:
                    day+=1
                    currw=weight
                else:
                    currw+=weight
            return day<=days

        while left <= right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                best_capacity = mid
                right = mid - 1
            else:
                left = mid + 1

        return best_capacity
