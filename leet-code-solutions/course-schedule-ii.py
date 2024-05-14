class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = [0 for i in range(numCourses+1)]   #we assume all courses have NO prerequest!
        graph = defaultdict(list)   #we will append the courses that have prerequests to the PREREQUISITEE!!
        queue = deque()
        order = []

        for x,y in prerequisites:
            incoming[x] += 1    #for those who have prequest increment +1
            graph[y].append(x)  #inorder to take x we need y so  

        for i in range(numCourses):  #if incoming is 0 it means we can process that(take that course) AND course that can be taken is appended to queue
            if incoming[i] == 0:
                queue.append(i)


        # since we appended course that are availabe to take(those with incoming of 0) we can pop them then we decrement incoming of other ones so that they will be available when their incoming becomes 0
        while queue:
            length = len(queue)
            for i in range(length):
                val = queue.popleft()
                order.append(val)

                neighbour = graph[val]
                for course in neighbour:
                    incoming[course] -= 1

                    if incoming[course] == 0:
                        queue.append(course)

        if len(order) != numCourses:    #if there are courses that are not on queue means there is cyle 
            return []

        return order

        
