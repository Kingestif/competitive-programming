class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        root = {i:i for i in range(n+1)}
        # changed the union code!!

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                root[y] = find(rootX)

        for x,y in edges:
            union(x,y)


        dic = defaultdict(int)
        for i in range(n):
            dic[find(i)] += 1

        print(dic)
        if len(dic) == 1:
            return find(0)
        return -1
