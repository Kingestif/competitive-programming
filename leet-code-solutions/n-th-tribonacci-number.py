class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        
        x = 0 
        y = 1 
        z = 1 
        ans = x + y + z

        for i in range(3,n):
            x = y 
            y = z
            z = ans
            ans = x + y + z
        return ans




