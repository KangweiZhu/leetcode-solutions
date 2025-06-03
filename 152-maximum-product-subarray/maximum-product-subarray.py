class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = len(nums)
        dp_min = [2**31 - 1 for _ in range(m)]
        dp_max = [-2**31 - 1 for _ in range(m)]
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        res = nums[0]
        
        for i in range(1, m):
            dp_min[i] = min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
            dp_max[i] = max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
            res = max(dp_min[i], dp_max[i], res)
        
        return res