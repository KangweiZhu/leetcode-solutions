class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            l
            le e
            lee ee e
        '''
        m = len(s)
        no_dup_wordDict = set(wordDict)
        dp = [False for _ in range(m + 1)]
        dp[0] = True

        for i in range(1, m + 1):
            for j in range(i):
                if s[j:i] in no_dup_wordDict and dp[j]:
                    dp[i] = True
        
        return dp[m]    