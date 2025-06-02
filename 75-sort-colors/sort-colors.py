class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        2 0 2 1 1 0
        
        0 0 2 1 1 2

        
        """
        m = len(nums)
        left = 0
        curr = 0
        right = m - 1
        
        while curr <= right:
            if nums[curr] == 0:
                temp = nums[curr]
                nums[curr] = nums[left]
                nums[left] = temp
                left += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                temp = nums[right]
                nums[right] = nums[curr]
                nums[curr] = temp
                right -= 1

        