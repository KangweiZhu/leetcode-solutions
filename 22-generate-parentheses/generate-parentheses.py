class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        temp_result = []

        def backtrack(left_par_len, right_par_len):
            if left_par_len == n and right_par_len == n:
                result.append(''.join(temp_result))
                return 
            
            if left_par_len < n:
                temp_result.append('(')
                backtrack(left_par_len + 1, right_par_len)
                temp_result.pop()
            
            if right_par_len < left_par_len:
                temp_result.append(')')
                backtrack(left_par_len, right_par_len + 1)
                temp_result.pop()
        
        backtrack(0, 0)
        return result
                