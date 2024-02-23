from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        time = 0
        for i in range(len(tickets)):
            queue.append(i)

        check=True
        while check:
            if queue[0] != k:
                if tickets[queue[0]] != 0:
                    time += 1
                    tickets[queue[0]] -= 1
                    queue.append(queue.popleft())
                else:
                    queue.append(queue.popleft())
            
            else:
                tickets[queue[0]] -= 1
                time += 1
                if tickets[queue[0]] <= 0:
                    return time
                else:
                    queue.append(queue.popleft())






        


                






        return 0



        