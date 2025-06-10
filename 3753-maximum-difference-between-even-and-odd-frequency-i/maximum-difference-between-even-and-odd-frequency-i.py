class Solution:
    def maxDifference(self, s: str) -> int:
        char_freq_map = Counter(s)
        max_o, min_e = -2**31, 2**31-1
        for k, v in char_freq_map.items():
            if v % 2 == 0:
                min_e = min(min_e, v)
            else:
                max_o = max(max_o, v)
        return max_o - min_e
        
        