class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = [0 for i in range(n+1)]   #we assume all courses have NO prerequest!
        graph = defaultdict(list)   #we will append the courses that have prerequests to the PREREQUISITEE!!
        queue = deque()
        order = [[]* i for i in range(n)]

        for x,y in edges:
            incoming[y] += 1    #for those who have prequest increment +1
            graph[x].append(y)  #inorder to take x we need y so  

        for i in range(n):  #if incoming is 0 it means we can process that(take that course) AND course that can be taken is appended to queue
            if incoming[i] == 0:
                queue.append(i)

        # since we appended course that are availabe to take(those with incoming of 0) we can pop them then we decrement incoming of other ones so that they will be available when their incoming becomes 0
        while queue:
            length = len(queue)
            for i in range(length):
                val = queue.popleft()

                neighbour = graph[val]
                for course in neighbour:
                    order[course].append(val)
                    for i in order[val]:
                        if i not in order[course]:
                            order[course].append(i)

                    incoming[course] -= 1

                    if incoming[course] == 0:
                        queue.append(course)

        for i in range(len(order)):
            order[i] = sorted(order[i])
        return order

