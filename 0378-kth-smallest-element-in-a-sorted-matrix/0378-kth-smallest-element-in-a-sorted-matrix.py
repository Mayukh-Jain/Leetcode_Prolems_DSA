class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        def count_less_or_equal(mid):
            count = 0
            row, col = n - 1, 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1 
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = low + (high - low) // 2
            
            if count_less_or_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low