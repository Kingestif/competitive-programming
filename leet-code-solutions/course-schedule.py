class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # grey means the node that called current node lay nw temelisen yemetanew so its cyle, but if its black yalekew node lay new temeliso yemetaw so no cycle
        map = defaultdict(list)
        color = defaultdict(int)

        for i in prerequisites:
            color[i[0]] = 'white'
            for j in range(1,len(i)):
                map[i[0]].append(i[j]) 
                color[i[j]] = 'white'

        is_cycle = False
        def DFS(node):
            nonlocal is_cycle
            neighbour = map[node]

            if is_cycle:
                return 

            color[node] = 'grey'
            for i in neighbour:
                if color[i] == 'white':
                    DFS(i)
                elif color[i] == 'grey':
                    is_cycle = True
            color[node] = 'black'

        print(map)
        print(color)

        keys = list(map.keys())
        for key in keys:
            DFS(key)
       





        if is_cycle:
            return False
        return True