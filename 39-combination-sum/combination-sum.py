class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        m = len(candidates)
        result = []
        temp_result = []
        
        def backtrack(start, curr_sum):
            if curr_sum == target:
                result.append(temp_result.copy())
                return
            if curr_sum > target:
                return
            for i in range(start, m):
                temp_result.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])
                temp_result.pop()
        
        backtrack(0, 0)
        return result