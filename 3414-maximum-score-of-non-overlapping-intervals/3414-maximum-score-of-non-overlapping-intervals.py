from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        A = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        n = len(A)
        ends = [x[1] for x in A]

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = A[i - 1]
            prev = bisect_left(ends, l)

            for k in range(1, 5):
                best_score, best_indices = dp[i - 1][k]

                prev_score, prev_indices = dp[prev][k - 1]
                new_score = prev_score + w
                
                new_indices = sorted(prev_indices + [idx])

                if new_score > best_score:
                    best_score = new_score
                    best_indices = new_indices
                elif new_score == best_score:
                    if best_indices == [] or new_indices < best_indices:
                        best_indices = new_indices

                dp[i][k] = (best_score, best_indices)

        return dp[n][4][1]