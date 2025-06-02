class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            q q q .
            q x q q
            q q q .
            . q . q

        '''
        chessboard = [['.'] * n for _ in range(n)]

        def isValid(curr_row, curr_col) -> bool:
            if curr_row < 0 or curr_col < 0 or curr_row >= n or curr_col >= n:
                return False
            
            # top left
            row_start = curr_row - 1
            col_start = curr_col - 1
            while row_start >= 0 and col_start >= 0:
                if chessboard[row_start][col_start] == 'Q':
                    return False
                row_start -= 1
                col_start -= 1

            # top right
            row_start = curr_row - 1
            col_start = curr_col + 1
            while row_start >= 0 and col_start < n:
                if chessboard[row_start][col_start] == 'Q':
                    return False
                row_start -= 1
                col_start += 1

            # vertical
            for i in range(n):
                if i != curr_row:
                    if chessboard[i][curr_col] == 'Q':
                        return False

            # horizontal
            for i in range(n):
                if i != curr_col:
                    if chessboard[curr_row][i] == 'Q':
                        return False
            
            return True
        
        result = []

        def backtrack(start_row):
            if start_row == n:
                result.append([''.join(row) for row in chessboard])
            for i in range(n):
                if isValid(start_row, i):
                    chessboard[start_row][i] = 'Q'
                    backtrack(start_row + 1)
                    chessboard[start_row][i] = '.'
        
        backtrack(0)
        return result
                