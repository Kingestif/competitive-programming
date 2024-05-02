class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # size = [1]*(n+1)
        # root = {i:i for i in range(1,n+1)}
        # weight = {(y,x):z for x,y,z in roads}
        # # print(weight)


        # def find(x):
        #     if x == root[x]:
        #         return x
        #     root[x] = find(root[x])
        #     return root[x]

        # def union(x, y):
        #     rootX = find(x)
        #     rootY = find(y)

        #     if rootX != rootY:
        #         if size[rootX] > size[rootY]:
        #             root[rootY] = rootX
        #             size[rootX] += size[rootY]
        #         else:
        #             root[rootX] = rootY
        #             size[rootY] += size[rootX]


        # ans = []
        # for x,y,z in roads:
        #     par1 = find(x)
        #     par2 = find(y)


        #     if par1 != par2:
        #         union(y,x)

        #     if par2 == 1 or par2 == n or par1 == 1 or par1 == n: 
        #         ans.append(weight[(y,x)])


        
        # print(weight)
        # print(root)
        # print(ans)
        # if len(ans) == 0:
        #     return 0
        # return min(ans)
        
        # using DFS
        map = defaultdict(list)
        visited = defaultdict(int)
        ans = []

        for x,y,z in roads:
            map[x].append((y,z))
            map[y].append((x,z))


        def DFS(node):
            if node in visited:
                return 
                
            neighbour = map[node]
            visited[node] = 1

            for i in neighbour:
                ans.append(i[1])
                DFS(i[0])


                    



        DFS(1)
        return min(ans)