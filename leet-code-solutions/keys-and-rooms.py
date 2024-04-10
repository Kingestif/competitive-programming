class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Just use cycle detection code, ONLY MODIFICATION is when we find cycle we make it to continue instead of returing b/c we want other nodes of the given dictionary key to be discovered
        map = defaultdict(list)
        visited = defaultdict(int)
       
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if i != rooms[i][j]:
                    map[i].append(rooms[i][j])



        color = {i : "white" for i in range(len(rooms))}
        is_cycle = True
        def DFS(node):
            visited[node] = 1
            nonlocal is_cycle

            color[node] = "grey"
            if node in map:
                for i in map[node]:
                    if color[i] == 'white':
                        DFS(i)
                    elif color[i] == 'grey':
                        is_cycle = False
                        continue    #ONLY MODIFICATION(check the blow commented test case why we do this instead of returning when we find cycle as always)
            color[node] = 'black'   #after visiting the nodes neighbours since there noting to visit make the node black


        DFS(0)
        return len(visited) == len(rooms)

        # [[2,3],[],[0],[1,3]]
