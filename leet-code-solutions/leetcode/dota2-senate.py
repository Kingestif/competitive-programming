from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rqueue = deque()
        Dqueue = deque()

        # make separate queue for R and D and store their index
        for i in range(len(senate)):
            if senate[i] == "R":
                Rqueue.append(i)
            else:
                Dqueue.append(i)

        # the one who becomes empty first will lose
        while len(Rqueue) > 0 and len(Dqueue) > 0:
            # first = Rqueue[0]    ; sec = Dqueue
            if Rqueue[0] < Dqueue[0]:   #means radiant comes first so its their turn to remove dires vote right
                Dqueue.popleft()
                Rqueue.append(Rqueue.popleft() + len(senate))

            else:
                Rqueue.popleft()
                Dqueue.append(Dqueue.popleft() + len(senate))

        
        if len(Rqueue) == 0:
            return "Dire"
        else:
            return "Radiant"

        


            
