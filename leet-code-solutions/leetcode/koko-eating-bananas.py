import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def API(mid):
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)

            if time > h:
                return False
            else:
                return True

        start = 1 ; end = max(piles) + 1
        while start <= end:
            mid = (start + end) //2 
            if API(mid):
                end = mid - 1
            else:
                start = mid + 1
        print(start,end)
        return start



