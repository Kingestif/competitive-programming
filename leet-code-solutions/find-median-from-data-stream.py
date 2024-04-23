import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []    ;   self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)

        if len(self.minHeap) != 0 and -self.maxHeap[0] > self.minHeap[0]:    #case1
            print("case",-self.maxHeap[0] ,self.minHeap[0])
            maxx = heappop(self.maxHeap)
            heappush(self.minHeap,-maxx)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            minn = heappop(self.minHeap)
            heappush(self.maxHeap,-minn)

        elif len(self.maxHeap) > len(self.minHeap) + 1:
            maxx = heappop(self.maxHeap)
            heappush(self.minHeap,-maxx)
            
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            return self.minHeap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


