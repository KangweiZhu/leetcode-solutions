class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            2 1 3
        '''
        result = []
        result_builder = []

        def backtrack():
            if len(result_builder) == len(nums):
                result.append(result_builder.copy())
                return
            for i in range(len(nums)):
                if nums[i] in result_builder:
                    continue
                else:
                    result_builder.append(nums[i])
                    backtrack()
                    result_builder.pop()
        
        backtrack()
        return result