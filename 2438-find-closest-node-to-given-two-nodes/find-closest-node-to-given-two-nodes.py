class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        m = len(edges)

        def getDistance(node):
            '''
                node: The current node

                Find the number of hops from the given node, to the rest of the nodes inside the graph.
            '''
            start = node
            dist = [-1] * m
            hop_num = 0
            visited = set()
            while start != -1 and start not in visited:
                dist[start] = hop_num
                hop_num += 1
                visited.add(start)
                start = edges[start]
            return dist
        
        dist1 = getDistance(node1)
        dist2 = getDistance(node2)
        
        '''
            For every node in the graph, check if node1 and node2 can visit it.
            If both of them can, then compare their distance to that node -- which one is larger.
            Then calculate the min value of this 'larger' result, for each node.
        '''
        result_idx = 2**31 - 1
        min_distance_seen = 2**31 - 1      
        for i in range(m):
            if dist1[i] != -1 and dist2[i] != -1:
                max_distance = max(dist1[i], dist2[i])
                if max_distance < min_distance_seen or (max_distance == min_distance_seen and i < result_idx): # As the problem stated, If there are multiple answers, return the node with the smallest index
                    min_distance_seen = max_distance
                    result_idx = i
        return -1 if result_idx == 2**31 - 1 else result_idx
            

            