from typing import List


class Solution:

  def stoneGameV(self, stoneValue: List[int]) -> int:
    n = len(stoneValue)
    if n <= 1:
      return 0

    # Prefix sum array for O(1) range sum calculations
    pref = [0] * (n + 1)
    for idx, val in enumerate(stoneValue):
      pref[idx + 1] = pref[idx] + val

    dp = [[0] * n for _ in range(n)]
    max_left = [[0] * n for _ in range(n)]
    max_right = [[0] * n for _ in range(n)]

    # Base cases for single elements
    for i in range(n):
      max_left[i][i] = stoneValue[i]
      max_right[i][i] = stoneValue[i]

    # Bottom-up interval DP
    for i in range(n - 1, -1, -1):
      mid = i
      for j in range(i + 1, n):
        total = pref[j + 1] - pref[i]

        # Monotonically advance mid where left_sum < total / 2
        while 2 * (pref[mid + 1] - pref[i]) < total:
          mid += 1

        if 2 * (pref[mid + 1] - pref[i]) == total:
          # Equal split: Alice can choose the best from either side
          ans = max(max_left[i][mid], max_right[mid + 1][j])
        else:
          # Left part is strictly smaller for k <= mid - 1
          left_ans = max_left[i][mid - 1] if mid > i else 0
          # Right part is strictly smaller for k >= mid (right subarray starts at mid + 1)
          right_ans = max_right[mid + 1][j] if mid + 1 <= j else 0
          ans = max(left_ans, right_ans)

        dp[i][j] = ans
        max_left[i][j] = max(max_left[i][j - 1], total + ans)
        max_right[i][j] = max(max_right[i + 1][j], total + ans)

    return dp[0][n - 1]