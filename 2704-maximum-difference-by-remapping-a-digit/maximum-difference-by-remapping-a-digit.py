class Solution:
    def minMaxDifference(self, num: int) -> int:
        stringnified_num = str(num)
        no_dup_digits_set = set(stringnified_num)

        max_num_seen = float('-inf')
        min_num_seen = float('inf')

        for d1 in no_dup_digits_set:
            for d2 in '0123456789':
                remapped_num = int(stringnified_num.replace(d1, d2))
                max_num_seen = max(max_num_seen, remapped_num)
                min_num_seen = min(min_num_seen, remapped_num)
        
        return max_num_seen - min_num_seen
        