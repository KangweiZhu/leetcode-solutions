class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        result = []
        temp_result = []
        
        def backtrack():
            if len(temp_result) == m:
                result.append(temp_result.copy())
                return
            for i in range(m):
                if nums[i] not in temp_result:
                    temp_result.append(nums[i])
                    backtrack()
                    temp_result.pop()

        backtrack()
        return result