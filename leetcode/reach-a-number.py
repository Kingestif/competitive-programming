class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0
        summ = 0

        while summ < target or (summ - target)%2 != 0:
            steps += 1
            summ += steps

        return steps 
        


        



        




