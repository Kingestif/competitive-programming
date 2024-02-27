class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # we can do it in one iteration by using below code(for even) but **n will take much time so we need to use power function to do that
        # return 5 ** n//2 * 4 ** n//2 works but TLE so refer Pow(x,n) leetcode question and use that for powering

        if n == 1:
            return 5

        if n % 2 == 0:
            return (self.myPow(5,n//2) )* (self.myPow(4,n//2)) % (10**9 + 7)
            

        else:
            return (self.myPow(5,n//2 + 1)) * (self.myPow(4,n//2)) % (10**9 + 7)

        
    def myPow(self, x: float, n: int) -> float:
        if n == 1:  
            return x
        elif n == 0:
            return 1    

        if n < 0:
            return 1 / self.myPow(x, abs(n))

        val = self.myPow(x,n//2)    
        if n % 2 == 0:
            ans = val * val 
        else:
            ans = val * val * x
        return ans  % (10**9 + 7)