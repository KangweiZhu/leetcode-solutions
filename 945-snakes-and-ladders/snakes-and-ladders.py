class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        
        value_row_col_dict = defaultdict()
        row = m - 1
        need_reverse = False
        value = 1
        while row >= 0:
            if not need_reverse:
                for col in range(n):
                    value_row_col_dict[value] = [row, col]
                    value += 1
            else:
                for col in range(n - 1, -1, -1):
                    value_row_col_dict[value] = [row, col]
                    value += 1
            need_reverse = not need_reverse
            row -= 1
        
        queue = deque()
        visited = set()
        visited.add(1)
        queue.append(1)
        step = 0
        
        def move(start_val, dice_val):
            next_val = min(start_val + dice_val, m * m)
            next_row, next_col = value_row_col_dict[next_val]
            if board[next_row][next_col] != -1:
                next_val = board[next_row][next_col]
            return next_val, next_row, next_col

        while queue:
            curr_level_size = len(queue)
            for i in range(curr_level_size):
                curr_val = queue.popleft()
                if curr_val == m * m:
                    return step
                for i in range(1, 7):
                    next_val, next_row, next_col = move(start_val=curr_val, dice_val=i)
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append(next_val)
            step += 1
        
        return -1