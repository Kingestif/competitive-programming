class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming = [0 for i in range(len(graph)+1)]
        edge = defaultdict(list)
        queue = deque()
        answer = []

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                incoming[i] += 1
                edge[graph[i][j]].append(i)

        for i in range(len(graph)):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            length = len(queue)
            for i in range(length):
                val = queue.popleft()
                answer.append(val)
                neighbour = edge[val]

                for path in neighbour:
                    incoming[path] -= 1

                    if incoming[path] == 0:
                        queue.append(path)


        answer.sort()
        return answer
