class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = [1]*(len(accounts)+1)
        root = {i:i for i in range(len(accounts)+1)}


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

        Acc = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in Acc:  #since it previously existed we have to union previously existed index with this ones index
                    union(i,Acc[accounts[i][j]])

                else:   #easy just add to the dictionary
                    Acc[accounts[i][j]] = i

        grp = defaultdict(list)
        for email,index in Acc.items():
            parent = find(index)
            grp[parent].append(email)


        ans = []
        for i,e in grp.items():
            name = accounts[i][0]
            ans.append([name] + sorted(grp[i]))

        return ans