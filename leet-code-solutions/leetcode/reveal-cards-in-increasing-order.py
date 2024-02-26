from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort()
        for i in deck:
            queue.append(i)
        print(queue)
        queue2 = deque()
        
        check = True
        while check and len(queue) > 0:
            if len(queue2) < 2:
                queue2.appendleft(queue.pop())
            else:
                queue2.appendleft(queue2.pop())
                queue2.appendleft(queue.pop())
        return queue2



