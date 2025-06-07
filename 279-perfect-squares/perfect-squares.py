class Solution:
    def numSquares(self, n: int) -> int:
        max_sqrt = int(math.sqrt(n))
        dp = [2**31-1 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n + 1):
            for j in range(max_sqrt + 1):
                if i < j * j:
                    continue
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]