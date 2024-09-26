class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = str(x)
        y = sum(map(int,list(y)))
        if x % y == 0:
            return y
            
        return -1
        