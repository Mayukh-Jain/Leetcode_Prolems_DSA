class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        idx = nums.index(0)

        is_inc = True
        for i in range(n):
            if nums[(idx + i) % n] != i:
                is_inc = False
                break

        is_dec = True
        for i in range(n):
            if nums[(idx - i + n) % n] != i:
                is_dec = False
                break

        if not is_inc and not is_dec:
            return -1

        res = float('inf')
        v = nums[0]

        if is_inc:
            res = min(res, (n - v) % n, v + 2 if v != 0 else 0)

        if is_dec:
            res = min(res, (v + 1) % n + 1, (n - v - 1) % n + 1)

        return int(res)