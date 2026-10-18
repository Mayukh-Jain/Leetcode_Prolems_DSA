import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def count_ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways_left = count_ways(left)
            ways_right = count_ways(right)
            
            interleave_ways = math.comb(len(left) + len(right), len(left))
            
            return (ways_left * ways_right * interleave_ways) % MOD
            
        return (count_ways(nums) - 1) % MOD