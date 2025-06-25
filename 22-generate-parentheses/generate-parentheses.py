class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            （（ 
        """
        result = []
        result_builder = []

        def backtrack(left_num, right_num):
            if left_num == 0 and right_num == 0:
                result.append(''.join(result_builder))
                return

            if left_num > 0:
                result_builder.append('(')
                backtrack(left_num - 1, right_num)
                result_builder.pop()

            if right_num > left_num:
                result_builder.append(')')
                backtrack(left_num, right_num - 1)
                result_builder.pop()
        
        backtrack(n, n)
        return result