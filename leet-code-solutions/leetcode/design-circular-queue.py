class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.arr=[0] * self.length
        self.start = -1
        self.end = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isEmpty(): 
            self.end = 0     #(0,0) means there is 1 e/t
            self.start = 0
            self.arr[self.end] = value

        elif self.isFull():
            return False

        else:
            self.end = (self.end + 1) % self.length
            self.arr[self.end] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        elif self.start == self.end:
            self.arr[self.start] = 0
            self.start = -1
            self.end = -1
    
        else:
            self.arr[self.start] = 0
            self.start = (self.start + 1) % self.length

        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.start == -1 and self.end == -1
        

    def isFull(self) -> bool:
        return self.start != -1 and (self.end + 1) % self.length == self.start
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()