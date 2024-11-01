class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for i in nums:
            heappush(heap, -i)


        summ = 0

        for i in range(k):
            val = -heappop(heap)
            summ += val
            heappush(heap, -math.ceil(val/3))

        return summ

