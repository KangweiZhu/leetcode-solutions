class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        result = []
        temp_result = []
        
        def backtrack(curr_size):
            if curr_size == m:
                result.append(temp_result.copy())
                return
            for i in range(m):
                if nums[i] not in temp_result:
                    temp_result.append(nums[i])
                    curr_size += 1
                    backtrack(curr_size)
                    temp_result.pop()
                    curr_size -= 1

        backtrack(0)
        return result