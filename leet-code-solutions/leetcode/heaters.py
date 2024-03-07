class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 1 based 
        # our function
        houses.sort() ; heaters.sort()
        def API(minimum):
            # use 2 pointers to check if the houses are within heater distance
            astart = 0 ; bstart = 0
            while astart < len(houses) and bstart < len(heaters):
                if houses[astart] >= heaters[bstart] - minimum and houses[astart] <= heaters[bstart] + minimum:
                    astart += 1
                else:
                    bstart += 1 

            if bstart == len(heaters): #our heaters are not enough
                return False
            return True

        start = 0 ; end = max(houses[-1],heaters[-1]) 
        while start <= end:
            mid = (start + end) // 2
            if API(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start


