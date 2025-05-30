class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtarget_idx_dict = defaultdict()
        for i, num in enumerate(nums):
            subtarget = target - num
            if subtarget in subtarget_idx_dict:
                return [subtarget_idx_dict[subtarget], i]
            else:
                subtarget_idx_dict[num] = i
        return [-1, -1]