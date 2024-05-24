class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        incoming = [0 for i in range(len(quiet))]   
        graph = defaultdict(list)   
        queue = deque()
        order = [i for i in range(len(quiet))]

        for x,y in richer:
            incoming[y] += 1    
            graph[x].append(y)   

        for i in range(len(quiet)):  
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                neighbour = graph[node]

                for val in neighbour:
                    incoming[val] -= 1

                    # the checking algorithm
                    if quiet[order[val]] > quiet[order[node]]:
                        order[val] = order[node]

                    if incoming[val] == 0:
                        queue.append(val)


        return order