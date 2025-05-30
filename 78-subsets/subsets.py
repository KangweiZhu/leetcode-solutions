class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  
        '''
            0 1    12    123     13      2
        '''
        m = len(nums)
        result = []
        temp_result = []

        def backtrack(start):
            result.append(temp_result.copy())
            for i in range(start, m):
                temp_result.append(nums[i])
                backtrack(i + 1)
                temp_result.pop()
        
        backtrack(0)
        return result