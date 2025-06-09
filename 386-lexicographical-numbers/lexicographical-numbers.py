class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(curr_num):
            result.append(curr_num)
            curr_num = curr_num * 10
            for i in range(0, 10):
                next_num = curr_num + i
                if next_num > n:
                    break
                dfs(next_num)
        
        for i in range(1, min(n, 9) + 1):
            dfs(i)
        
        return result
