class Solution:
    def robotWithString(self, s: str) -> str:
        m = len(s)
        min_suffix = ['~' for _ in range(m)]
        min_suffix[m - 1] = s[m - 1]
        for i in range(m - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        t = []
        p = []
        for i in range(m):
            t.append(s[i])
            while t and (i == m - 1 or t[-1] <= min_suffix[i + 1]):
                p.append(t.pop())
        return ''.join(p)
                
