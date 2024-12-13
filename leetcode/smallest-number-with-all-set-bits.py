class Solution:
    def smallestNumber(self, n: int) -> int:
        while len(set(list(bin(n)[2:]))) != 1:
            n += 1
        
        return n
        