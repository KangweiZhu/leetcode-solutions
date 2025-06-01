class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for a in range(min(n, limit) + 1):
            b_lowerbound = max(0, n - a - limit)
            b_upperbound = min(n - a, limit)
            if b_lowerbound <= b_upperbound:
                count += b_upperbound - b_lowerbound + 1
        return count