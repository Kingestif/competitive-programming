import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:k]
        heapify(self.nums)

        for i in range(k,len(nums)):
            if nums[i] > self.nums[0]:
                heappop(self.nums)
                heappush(self.nums,nums[i])
        
        # this will do the largest kth for first parameters
        

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums,val)

        elif val > self.nums[0]:
            heappop(self.nums)
            heappush(self.nums,val)

        return self.nums[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)