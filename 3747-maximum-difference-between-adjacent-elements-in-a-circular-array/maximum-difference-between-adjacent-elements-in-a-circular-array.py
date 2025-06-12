class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_dist = 0
        m = len(nums)
        for i in range(m - 1):
            max_dist = max(max_dist, abs(nums[i + 1] - nums[i]))
        if m > 1:
            max_dist = max(abs(nums[-1] - nums[0]), max_dist)
        return max_dist