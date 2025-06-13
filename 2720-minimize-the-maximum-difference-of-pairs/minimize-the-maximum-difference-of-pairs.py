from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        # 判断是否能在最大差为 max_diff 的前提下，找到至少 p 对不重复的配对
        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # 跳过这两个数
                else:
                    i += 1  # 当前不能配对，尝试下一个
            return count >= p

        # 二分搜索答案
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left
