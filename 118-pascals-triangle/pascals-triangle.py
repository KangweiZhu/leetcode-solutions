class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        m = numRows
        dp = []

        for i in range(m):
            curr_level_len = i + 1
            ptr = 0
            curr_level_container = []
            while ptr < curr_level_len:
                if ptr == 0 or ptr == curr_level_len - 1:
                    curr_level_container.append(1)
                else:
                    curr_level_container.append(dp[i - 1][ptr] + dp[i - 1][ptr - 1])
                ptr += 1
            dp.append(curr_level_container)
        
        return dp
            