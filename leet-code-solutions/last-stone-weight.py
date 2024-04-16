import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heap = nlargest(2,stones)
            if heap[0] == heap[1]:
                stones.remove(heap[0])
                stones.remove(heap[1])
            elif heap[0] < heap[1]:
                stones.remove(heap[0])
                idx = stones.index(heap[1])
                stones[idx] -= heap[0]
            else:
                stones.remove(heap[1])
                idx = stones.index(heap[0])
                stones[idx] -= heap[1]
        print(stones)
        if len(stones) < 1:
            return 0
        return stones[0]