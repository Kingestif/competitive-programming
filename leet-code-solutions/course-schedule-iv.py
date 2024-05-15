class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # # using unionfind
        # root = {i:i for i in range(numCourses+1)}
        # check = defaultdict(list)

        # # simplified unionfind
        # def find(x):
        #     if x == root[x]:
        #         return x
        #     root[x] = find(root[x])
        #     return root[x]

        # def union(x, y):
        #     rootX = find(x)
        #     rootY = find(y)

        #     if rootX != rootY:
        #         root[rootY] = rootX
        #         return True
        #     else:
        #         return False

        # for x,y in prerequisites:
        #     union(x,y)

        # print(root)
        # ans = []

        # for x,y in queries:
        #     if find(y) == x:
        #         ans.append(True)
        #     else:
        #         ans.append(False)

                

        # return ans
        map = defaultdict(list)
        check = defaultdict(int)

        for x,y in prerequisites:
            map[y].append(x)

        def DFS(node,val):
            neighbour = map[node]
            for i in neighbour:
                if i == val:
                    # print(i,val)
                    return True
                if i not in check:
                    check[i] += 1
                    if DFS(i,val):
                        return True

            return False



        ans = []
        for x,y in queries:
            check = defaultdict(int)
            if DFS(y,x):
                ans.append(True)
            else:
                ans.append(False)
                

        print(map)
        print(check)
        return ans




















