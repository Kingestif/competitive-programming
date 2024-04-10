class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        map = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    map[i+1].append(j+1)

        def DFS(node):
            check[node] += 1
            neighbours = map[node]

            for i in neighbours:
                if i not in check:
                    DFS(i)


        check = defaultdict(int)
        count = 0
        for key,values in map.items():
            if key not in check:
                count += 1
                DFS(key)

        return count







