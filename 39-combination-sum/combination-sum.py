class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        result_builder = []
        m = len(candidates)

        def backtrack(start, curr_sum):
            if curr_sum == target:
                result.append(result_builder.copy())
                return 
            if curr_sum > target:
                return
            for i in range(start, m):
                result_builder.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])
                result_builder.pop()
        
        backtrack(0, 0)
        return result