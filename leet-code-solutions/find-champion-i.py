class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # when you union make the winner root of the loser
        # finally all of their root will be the winner
        root = {i:i for i in range(len(grid)+1)}

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                root[rootY] = rootX

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    union(i,j)

        return find(0)


            