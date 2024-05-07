import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # assumes the tasks are in sorted manner 
        # so to fix that just enumerate over it to hold on the original indexes then sort it based on the first value!!, then use tasks[i][2] to access the orginal index insted of just "i"
        
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t: t[0])

        end = tasks[0][0]
        heap = []
        ans = []

        i = 0
        while i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= end:
                heappush(heap,(tasks[i][1],tasks[i][2]))    #changed "i" to tasks[i][2] 
                i += 1

            if len(heap) > 0:
                val = heappop(heap)
                ans.append(val[1])
                end += val[0]
            else:
                end = tasks[i][0]

        while len(heap) != 0:
            val = heappop(heap)
            ans.append(val[1])

        return ans


