class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # 1. making the adjacency list
        visited = defaultdict(int)

        map = defaultdict(list)
        for i in edges:
            map[i[0]].append(i[1])
            map[i[1]].append(i[0])

        def DFS(node):
            if node == destination:
                return True

            neighbour = map[node]
            visited[node] = 1
            for i in neighbour:
                if i == destination:    #additional case
                    return True

                if i not in visited:
                    visited[i] = 1
                    if DFS(i):      #this condition is MUST!!
                        return True

        # iterate through the list and pass to the function but for this problem since we are asked to start from source we jsut need to call DFS only once
        if DFS(source):
            return True
        return False
