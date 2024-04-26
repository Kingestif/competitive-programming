class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = [1]*(len(edges)+1)
        root = {i:i for i in range(len(edges)+1)}


        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]


        for x,y in edges:
            val1 = find(x)
            val2 = find(y)

            if val1 != val2:
                union(x,y)
            else:
                return [x,y]
