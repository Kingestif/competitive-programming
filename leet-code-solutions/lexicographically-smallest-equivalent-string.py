class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        size = [1]*(len(s1)-1)
        root = defaultdict(int)

        for i in range(len(s1)):
            root[s1[i]] = s1[i]
            root[s2[i]] = s2[i]

        for i in range(len(baseStr)):
            root[baseStr[i]] = baseStr[i]

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if ord(rootX) < ord(rootY):
                root[rootY] = rootX
            else:
                root[rootX] = rootY

        for i in range(len(s1)):
            x = find(s1[i])
            y = find(s2[i])

            if x != y:
                union(x,y)

        ans = ""
        for i in range(len(baseStr)):
            print(ans,baseStr[i],root[baseStr[i]])
            ans += find(root[baseStr[i]])

        return ans
