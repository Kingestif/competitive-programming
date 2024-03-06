class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # time complexity: the binary search(o(N)) and loop O(n) = NlogN
        def API(mid):
           counter = 1 ; total = 0
           for i in range(len((weights))):
               if total + weights[i] <= mid:
                   total += weights[i]
               else:
                   counter += 1
                   total = 0
                   if weights[i] > mid:
                       return False
                   total = weights[i]
           if counter > days:
               return False
           return True

        # ---------binary search
        start = max(weights) #minimum weight we can ship
        end = sum(weights)+1  #maximum weight we can ship
        while start <= end:
            mid = (start + end) // 2
            if API(mid):    #true
                end = mid - 1
            else:
                start = mid + 1

        return start
        

       
        






