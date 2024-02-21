class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        rem=0 ; counter = 0 
        while target >=1:
            if maxDoubles > 0:
                if target//2 >= 1:
                    maxDoubles -= 1
                    counter += 1
                    if target % 2 != 0:
                        rem += 1
                    target = target//2
                else:
                    counter += (target - 1)
                    break
            else:
                counter += (target -1)
                break
        return counter + rem





               