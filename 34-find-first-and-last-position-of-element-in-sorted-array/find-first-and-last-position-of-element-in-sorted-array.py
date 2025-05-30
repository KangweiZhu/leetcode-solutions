class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
            target exist/no exist
            target in left/right/mid/left-mid/mid-right
            single/multi target
            1 2 2 2 3 3 4 5 6
        '''
        m = len(nums)
        left = 0
        right = m - 1
        
        def find_first(left, right):
            first = -1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    first = mid
                    right = mid - 1 # prior to search left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def find_second(left, right):
            last = -1
            while left <= right:
                mid = (right + left) >> 1
                if nums[mid] == target:
                    last = mid
                    left = mid + 1 # prior to search right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        return [find_first(left, right), find_second(left, right)]