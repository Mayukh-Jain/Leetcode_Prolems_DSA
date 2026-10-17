class SegmentTree:
    def __init__(self, n: int):
        self.sum = [0] * (4 * n)
        self.sq_sum = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def push(self, node: int, length: int) -> None:
        if self.lazy[node]:
            lazy_val = self.lazy[node]
            left = 2 * node + 1
            right = 2 * node + 2
            
            len_left = length - length // 2
            self.sq_sum[left] = (self.sq_sum[left] + 2 * lazy_val * self.sum[left] + lazy_val * lazy_val * len_left) % self.MOD
            self.sum[left] = (self.sum[left] + lazy_val * len_left) % self.MOD
            self.lazy[left] += lazy_val
            
            len_right = length // 2
            self.sq_sum[right] = (self.sq_sum[right] + 2 * lazy_val * self.sum[right] + lazy_val * lazy_val * len_right) % self.MOD
            self.sum[right] = (self.sum[right] + lazy_val * len_right) % self.MOD
            self.lazy[right] += lazy_val
            
            self.lazy[node] = 0

    def update(self, node: int, start: int, end: int, l: int, r: int, val: int) -> None:
        if l <= start and end <= r:
            length = end - start + 1
            self.sq_sum[node] = (self.sq_sum[node] + 2 * val * self.sum[node] + val * val * length) % self.MOD
            self.sum[node] = (self.sum[node] + val * length) % self.MOD
            self.lazy[node] += val
            return
            
        self.push(node, end - start + 1)
        mid = (start + end) // 2
        
        if l <= mid:
            self.update(2 * node + 1, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 2, mid + 1, end, l, r, val)
            
        self.sum[node] = (self.sum[2 * node + 1] + self.sum[2 * node + 2]) % self.MOD
        self.sq_sum[node] = (self.sq_sum[2 * node + 1] + self.sq_sum[2 * node + 2]) % self.MOD

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        ans = 0
        MOD = 10**9 + 7
        
        for i, x in enumerate(nums):
            start = last_seen.get(x, -1) + 1
            
            tree.update(0, 0, n - 1, start, i, 1)
            
            ans = (ans + tree.sq_sum[0]) % MOD
            
            last_seen[x] = i
            
        return ans