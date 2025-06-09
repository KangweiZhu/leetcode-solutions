class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr_num = 1
        curr_steps = 1  

        def get_steps(curr_num):
            curr_prefix = curr_num
            curr_end = curr_prefix
            count = 0
            while curr_prefix <= n:
                steps = min(n, curr_end) - curr_prefix + 1
                count += steps
                curr_prefix *= 10
                curr_end = curr_end * 10 + 9
            return count

        while curr_steps < k:
            curr_prefix_nums = get_steps(curr_num)
            if curr_steps + curr_prefix_nums <= k:
                curr_num += 1
                curr_steps += curr_prefix_nums
            else:
                curr_num *= 10
                curr_steps += 1
        
        return curr_num
