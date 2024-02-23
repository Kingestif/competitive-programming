class RecentCounter:

    def __init__(self):
        self.arr=[]

    def ping(self, t: int) -> int:
        num = t - 3000
        self.arr.append(t)
        for i in range(len(self.arr)):
            if self.arr[i] >= num:
                return len(self.arr) - i
        return 0
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)