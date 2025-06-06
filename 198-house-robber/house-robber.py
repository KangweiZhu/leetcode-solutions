class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [0 for _ in range(m)]
        
        if m == 0:
            return 0
        
        if m == 1:
            return nums[0]
        
        if m == 2:
            return max(nums[0],nums[1])
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, m):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[m - 1]

