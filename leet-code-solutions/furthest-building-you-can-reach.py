import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # refer Neetcode
        heap = []
        tall = []
        for i in range(len(heights)-1):
            tall.append(heights[i+1] - heights[i])

        for i in range(len(tall)):
            if tall[i] < 0:
                continue
            bricks -= tall[i]
            heappush(heap,-tall[i])
        
            if bricks < 0:
                if ladders == 0:
                    return i   

                ladders -= 1
                val = heappop(heap)
                bricks += -val 
                

        return len(heights) - 1
