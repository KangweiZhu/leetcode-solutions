class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            1 2 3 4 
        '''
        m = len(nums)
        left = 0
        right = m - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]