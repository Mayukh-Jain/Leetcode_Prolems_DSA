class Solution:

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = {}

        for char in s:
            dp[char] = (sum(dp.values()) + 1) % MOD

        return sum(dp.values()) % MOD