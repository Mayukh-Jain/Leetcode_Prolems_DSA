class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        min_length = float("inf")
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                min_length = min(min_length, r - l + 1)
                current_sum -= nums[l]
                l += 1

        return min_length if min_length != float("inf") else 0