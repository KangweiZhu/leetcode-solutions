class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board:
            return -1
        
        m = len(board)
        n = len(board[0])
        max_val = m * m

        # Construct a mapping of the blocks real value with its row,col
        value_row_col_dict = defaultdict(list)
        value = 1
        need_reverse = False
        row = m - 1
        while row >= 0:
            if not need_reverse:
                for col in range(n):
                    value_row_col_dict[value] = [row, col]
                    value += 1
            else:
                for col in range(n - 1, -1, -1):
                    value_row_col_dict[value] = [row, col]
                    value += 1
            row -= 1
            need_reverse = not need_reverse

        def move(curr_val, dice_val):
            if dice_val > 6:
                raise ValueError(f'Dice should be only rolled from 1 to 6, now is {val}!')
            next_val = min(max_val, curr_val + dice_val)
            next_row, next_col = value_row_col_dict[next_val]
            return next_val, next_row, next_col
        
        min_num_hops = 2**31 - 1
        start_val = 1
        visited = set()

        def dfs(start_val, num_hops):
            nonlocal min_num_hops
            if start_val == max_val:
                min_num_hops = min(min_num_hops, num_hops)
                return 
            for i in range(1, 7):
                next_val, next_row, next_col = move(curr_val=start_val, dice_val=i)
                if board[next_row][next_col] != -1:
                    next_val = board[next_row][next_col]
                if next_val not in visited:
                    visited.add(next_val)
                    dfs(start_val=next_val, num_hops=num_hops + 1)
                    visited.remove(next_val)

        # visited.add(1)
        # dfs(1, 0)
        
        visited.add(1)
        queue = deque()
        queue.append(1)
        min_num_hops = 0
        
        while queue:
            curr_level_len = len(queue)
            for i in range(curr_level_len):
                start_val = queue.popleft()
                if start_val == max_val:
                    return min_num_hops
                for i in range(1, 7):
                    next_val, next_row, next_col = move(curr_val=start_val, dice_val=i)
                    if board[next_row][next_col] != -1:
                        next_val = board[next_row][next_col]
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append(next_val)
            min_num_hops += 1
        return min_num_hops if start_val == max_val else -1