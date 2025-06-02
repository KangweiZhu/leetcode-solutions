class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
            m = 3
            [1,0,2]
            [1,1,2]

            [1,3,4,5,2]
            
            [1,2,3,4,1]
        """
        m = len(ratings)
        candy_distribution = [1 for _ in range(m)]
        
        for i in range(m - 1):
            if ratings[i + 1] > ratings[i]:
                candy_distribution[i + 1] = candy_distribution[i] + 1

        for i in range(m - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_distribution[i - 1] = max(candy_distribution[i - 1], candy_distribution[i] + 1)

        return sum(candy_distribution)
