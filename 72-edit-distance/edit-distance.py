class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
          ' v b c
        ' 0 1 2 3
        a 1 1 x x
        b 2 x x x
        c 3 x x x
        '''
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] + 1
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] + 1
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(
                            dp[i - 1][j],
                            dp[i][j - 1],
                            dp[i - 1][j - 1]
                        ) + 1
        return dp[m][n]