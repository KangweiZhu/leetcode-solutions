class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mov_unit = [1, -1]
        visited = set()
        word_len = len(word)
        m = len(board)
        n = len(board[0])
        found = False

        def dfs(curr_row, curr_col, curr_idx):
            nonlocal found
            if curr_idx == word_len:
                found = True
                return
            if curr_row >= m or curr_row < 0 or curr_col >= n or curr_col < 0 or board[curr_row][curr_col] != word[curr_idx]:
                return 
            temp = board[curr_row][curr_col]
            board[curr_row][curr_col] = '#'
            dfs(curr_row + 1, curr_col, curr_idx + 1)
            dfs(curr_row, curr_col + 1, curr_idx + 1)
            dfs(curr_row - 1, curr_col, curr_idx + 1)
            dfs(curr_row, curr_col - 1, curr_idx + 1)
            board[curr_row][curr_col] = temp
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
        
        return found
            
            
            