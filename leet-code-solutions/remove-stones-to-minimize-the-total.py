import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # using max heap
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]

        heapify(piles)
        
        for i in range(k):
            num = piles[0]
            heappop(piles)
            heappush(piles,math.floor(num/2))
        return abs(sum(piles))



        print(piles)
        return 0