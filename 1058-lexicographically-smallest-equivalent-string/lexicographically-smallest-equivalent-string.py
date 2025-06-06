class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(list)
        
        for ch1, ch2 in zip(s1, s2):
            graph[ch1].append(ch2)
            graph[ch2].append(ch1)
        
        def bfs(ch):
            visited = set()
            visited.add(ch)
            
            group = []
            group.append(ch)
            
            queue = deque()
            queue.append(ch)
            
            while queue:
                curr_level_len = len(queue)
                for i in range(curr_level_len):
                    curr_char = queue.popleft()
                    for neighbor in graph[curr_char]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                            group.append(neighbor)
            
            smallest_char = min(group)
            return smallest_char
        
        res = ''
        for ch in baseStr:
            res += (bfs(ch))
        return res
        
                        
                        

            

