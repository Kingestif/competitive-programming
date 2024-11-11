class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
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
                        continue  
            color[node] = 'black'  


        DFS(0)
        return len(visited) == len(rooms)

