class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            current_sum = 0
            
            for X in range(1, 4):
                if i + X - 1 < n:
                    current_sum += stoneValue[i + X - 1]
                    diff = current_sum - dp[(i + X) % 4]
                    if diff > max_diff:
                        max_diff = diff
            
            dp[i % 4] = max_diff

        alice_diff = dp[0]

        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"