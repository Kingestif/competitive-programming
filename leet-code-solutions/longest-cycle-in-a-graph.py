class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        cycle = set() #being visited is not enough to be cycle b/c separate DFS calls can result visiting VIsited nodes even though there were not cycle
        ans = [-1]
        distance = defaultdict(int)

        def DFS(node,dist):
            if node != -1:
                if node not in visited:
                    cycle.add(node)
                    visited.add(node)
                    distance[node] = dist
                    DFS(edges[node],dist+1)
                elif node in cycle:
                    ans.append(dist - distance[node])

                cycle.discard(node)

        for i in range(len(edges)):
            dist = 0
            DFS(i,dist)

        return max(ans)


