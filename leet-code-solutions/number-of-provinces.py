class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # # there are unconnected Nodes so run DFS using loop instead of only running it once
        # # USE DFS to do this

        # map = defaultdict(list)
        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[i])):
        #         if isConnected[i][j] == 1:
        #             map[i+1].append(j+1)

        # def DFS(node):
        #     check[node] += 1
        #     neighbours = map[node]

        #     for i in neighbours:
        #         if i not in check:
        #             DFS(i)


        # check = defaultdict(int)
        # count = 0
        # for key,values in map.items():
        #     if key not in check:
        #         count += 1
        #         DFS(key)

        # return count


        # using union Find
        root = {i:i for i in range(len(isConnected))}
        size = {i:1 for i in range(len(isConnected))}

        def find(x):
            if x == root[x]:    #if nodes representative is itself then we find the root parent
                return x
            
            return find(root[x])

        def union(x,y):
            rootX = find(x) #if we just say root[x] we might not find the absolute root so use find to find the last possible root of the node
            rootY = find(y) 
            print(x,rootX, y,rootY)

            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]



        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i,j)

        check = set()
        for key,values in root.items():
            val = find(key)
            if val not in check:
                check.add(val)
            
            

        return len(check)







