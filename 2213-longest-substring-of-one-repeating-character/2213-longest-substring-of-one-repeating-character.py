from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # Segment tree arrays
        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_pchar = [''] * (4 * n)
        tree_schar = [''] * (4 * n)

        def merge(node: int, left: int, right: int, l: int, mid: int, r: int):
            left_len = mid - l + 1
            right_len = r - mid
            
            # Prefix computation
            tree_pchar[node] = tree_pchar[left]
            tree_pref[node] = tree_pref[left]
            if tree_pref[left] == left_len and tree_pchar[left] == tree_pchar[right]:
                tree_pref[node] += tree_pref[right]
            
            # Suffix computation
            tree_schar[node] = tree_schar[right]
            tree_suff[node] = tree_suff[right]
            if tree_suff[right] == right_len and tree_schar[right] == tree_schar[left]:
                tree_suff[node] += tree_suff[left]
            
            # Max length computation
            tree_max[node] = max(tree_max[left], tree_max[right])
            if tree_schar[left] == tree_pchar[right]:
                tree_max[node] = max(tree_max[node], tree_suff[left] + tree_pref[right])

        def build(node: int, l: int, r: int):
            if l == r:
                tree_max[node] = 1
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_pchar[node] = s[l]
                tree_schar[node] = s[l]
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, 2 * node, 2 * node + 1, l, mid, r)

        def update(node: int, l: int, r: int, idx: int, char: str):
            if l == r:
                tree_pchar[node] = char
                tree_schar[node] = char
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, r, idx, char)
            merge(node, 2 * node, 2 * node + 1, l, mid, r)

        # Build initial tree
        build(1, 0, n - 1)
        
        # Process queries
        ans = []
        for idx, char in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, char)
            ans.append(tree_max[1])  # Root node contains max length for range [0, n-1]
            
        return ans