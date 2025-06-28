class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            [1,2,3]
            [[], [1], [2], [3], [1,2], [1,3],[2,3], [1,2,3]]
        '''
        result = []
        result_builder = []
        
        def backtrack(start):
            result.append(result_builder.copy())
            '''
                [], [1], [1,2], [1,2,3], [1,3], [2], [2,3],[3]
            '''
            for i in range(start, len(nums)):
                result_builder.append(nums[i])
                backtrack(i + 1)
                result_builder.pop()
        
        backtrack(0)
        return result