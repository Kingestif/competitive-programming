class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = defaultdict(list)
        for course,pre in prerequisites:
            map[course].append(pre)
        ans = []
        check = {}

        def DFS(node):
            if node in check:
                return check[node]


            check[node] = True
            neighbour = map[node]

            for i in neighbour:
                if DFS(i):
                    return
            check[node] = False
            ans.append(node)

            






        for i in range(numCourses):
            if DFS(i):
                return []


        return ans