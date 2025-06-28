class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        result_builder = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(row, col):
            # top left
            tmp_row = row - 1
            tmp_col = col - 1
            while tmp_row >= 0 and tmp_col >= 0:
                if result_builder[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row -= 1
                tmp_col -= 1
            
            # top right 
            tmp_row = row - 1
            tmp_col = col + 1
            
            while tmp_row >= 0 and tmp_col < n:
                if result_builder[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row -= 1
                tmp_col += 1
            
            # vertically above
            tmp_row = row -1
            tmp_col = col
            while tmp_row >= 0:
                if result_builder[tmp_row][tmp_col] == 'Q':
                    return False
                tmp_row -= 1

            return True
            
        def backtrack(row_num):
            if row_num == n:
                result.append([''.join(row_elements) for row_elements in result_builder])
                return 
            for i in range(n):
                if isValid(row_num, i):
                    result_builder[row_num][i] = 'Q'
                    backtrack(row_num + 1)
                    result_builder[row_num][i] = '.'

        backtrack(0)
        return result

        
    