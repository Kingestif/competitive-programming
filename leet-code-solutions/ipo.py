class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        check = [] 
        heap = []

        for i in range(len(profits)):
            check.append((capital[i],profits[i]))

        check.sort()
        # print(check)

        # for i in range(len(check)):
        i = 0
        while k > 0 and i < len(profits):
            if check[i][0] <= w:
                heappush(heap,-check[i][1])
                i += 1
            else:
                if len(heap) <= 0:
                    break
                prof = heappop(heap)
                prof = -prof
                w += prof
                k -= 1

        # return w
        if len(heap) == 0:
            return w
        else:
            while k > 0 and len(heap) > 0:
                w += -heappop(heap)
                k -= 1

        return w

