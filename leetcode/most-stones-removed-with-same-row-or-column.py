class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {i:i for i in range(len(stones)+1)}
        similar = []

        # simplified unionfind
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
                return True
            else:
                return False

        # to find indexes that share same column or row
        def same(p1,p2):
            if p1[0] == p2[0] or p1[1] == p2[1]:
                return True


        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if same(stones[i],stones[j]):
                    similar.append((i,j))


        # call union find on those indexes
        ans = 0
        for x,y in similar:
            if union(x,y):
                ans += 1
        return ans


                