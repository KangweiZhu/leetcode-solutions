class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
            babab
        '''
        if not s:
            return ''

        m = len(s)
        longest_p_len = 1
        longest_p = s[0]
        
        dp = [[False] * m for _ in range(m)]
        
        for i in range(m):
            dp[i][i] = True
        
        for i in range(m - 1):
            if s[i] == s[i + 1]:
                longest_p = s[i:i+2]
                longest_p_len = 2    
                dp[i][i + 1] = True
        
        for i in range(3, m + 1):
            for j in range(m - i + 1):
                end = j + i - 1
                if s[j] == s[end] and dp[j + 1][end - 1]:
                    dp[j][end] = True
                    if i > longest_p_len:
                        longest_p_len = i
                        longest_p = s[j:end+1]
        
        return longest_p