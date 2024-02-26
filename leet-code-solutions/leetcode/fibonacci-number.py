class Solution:
    def fib(self, n: int) -> int:
        if n == 0:  #2 base cases
            return 0
        elif n == 1:
            return 1 

        return self.fib(n-1) + self.fib(n-2)
        # this 2 functoins are not called simultaneously after fib(n-1) reach the base case the second(fib(n-2)) will be called
        