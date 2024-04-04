class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # adjacency list
        color = [-1 for _ in range(len(graph))]
        visited = defaultdict(int)
        map = defaultdict(list)
        for i in range(len(graph)):
            map[i] = graph[i]

        print(map)
        is_bipartite = True

        def DFS(key):
            nonlocal is_bipartite
            neighbour = map[key]

            
            for i in neighbour:
                print("i",i)
                if color[i] == -1:
                    if color[key] == 0:
                        color[i] = 1
                    else:
                        color[i] = 0
                    is_bipartite = is_bipartite and DFS(i)
                else:
                    is_bipartite = is_bipartite and color[key] != color[i]

            return is_bipartite



        result = True
        for key in map:
            if color[key] == -1:
                color[key] = 0

                result = result and DFS(key)

        return result
