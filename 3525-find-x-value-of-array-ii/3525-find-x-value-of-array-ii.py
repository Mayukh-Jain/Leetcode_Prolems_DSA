from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [(1, {}) for _ in range(4 * self.n)]
        if self.n > 0:
            self.build(nums, 0, 0, self.n - 1)

    def merge(self, left_node, right_node):
        l_prod, l_freq = left_node
        r_prod, r_freq = right_node
        
        res_prod = (l_prod * r_prod) % self.k
        
        res_freq = l_freq.copy()
        
        for p, count in r_freq.items():
            np = (l_prod * p) % self.k
            res_freq[np] = res_freq.get(np, 0) + count
            
        return (res_prod, res_freq)

    def build(self, nums: List[int], node: int, start: int, end: int):
        if start == end:
            val = nums[start] % self.k
            self.tree[node] = (val, {val: 1})
            return
        
        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            v = val % self.k
            self.tree[node] = (v, {v: 1})
            return
            
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
            
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node: int, start: int, end: int, ql: int, qr: int):
        if ql <= start and end <= qr:
            return self.tree[node]
        
        mid = (start + end) // 2
        
        if qr <= mid:
            return self.query(2 * node + 1, start, mid, ql, qr)
        elif ql > mid:
            return self.query(2 * node + 2, mid + 1, end, ql, qr)
        else:
            left_res = self.query(2 * node + 1, start, mid, ql, qr)
            right_res = self.query(2 * node + 2, mid + 1, end, ql, qr)
            return self.merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
            
        seg_tree = SegmentTree(nums, k)
        ans = []
        
        for q in queries:
            idx, val, start, x = q
            
            seg_tree.update(0, 0, n - 1, idx, val)
            
            if start >= n:
                ans.append(0)
                continue
                
            _, freq = seg_tree.query(0, 0, n - 1, start, n - 1)
            ans.append(freq.get(x, 0))
            
        return ans