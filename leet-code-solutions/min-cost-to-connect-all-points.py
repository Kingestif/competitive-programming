class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        root = {i:i for i in range(len(points)+1)}

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

        def getDis(p1,p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        path = []       #store the difference in distance

        # pair all points to eachother to find the minimum distance
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                path.append((getDis(points[i],points[j]), i, j))

        path.sort() #since we need the minimum distance to be at front

        # finally do union find on the index's of above path if union return True we add the distance since we only union once the smallest ones
        ans = 0
        for x,y,z in path:
            if union(y,z):
                ans += x
        return ans

                