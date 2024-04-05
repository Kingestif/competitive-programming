"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map = defaultdict(int)
        visited = defaultdict(int)
        for i in range(len(employees)):
            map[employees[i].id] = (employees[i].subordinates, employees[i].importance)

        total = 0
        def DFS(node):
            nonlocal total
            neighbour = map[node][0]
            total += map[node][1]
            visited[node] = 1

            for i in neighbour:
                if i not in visited:
                    DFS(i)



        DFS(id)
        return total 



