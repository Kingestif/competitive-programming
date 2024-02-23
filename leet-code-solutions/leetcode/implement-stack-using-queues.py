from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        counter = 0
        # print("before",self.queue)
        while counter < len(self.queue) - 1:  #O(N)
            self.queue.append(self.queue.popleft())
            counter += 1
        # print("after",self.queue)
        return 0

    def pop(self) -> int:
        # print("ok",self.queue)
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()