class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1st do the base case (**known) we have power of 1 gives number itself AND power of 0 gives 1 
        if n == 1:  
            return x
        elif n == 0:
            return 1

        # edge case(x power of -2 means 1/x**positive 2)
        if n < 0:
            return 1 / self.myPow(x, abs(n))

        # MAIN: if even exponent can be divided into 2 groups ex 3**4 = 3**2 * 3**2
                # if odd exponent can be divided into 3 groups ex 3**5 = 3**2 * 3**2 * 3
        val = self.myPow(x,n//2)    #to minimize repetition
        if n % 2 == 0:
            return val * val 
        else:
            return val * val * x