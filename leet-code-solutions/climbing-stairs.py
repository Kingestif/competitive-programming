class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        def climb(n):
            if n == 0 or n == 1 or n == 2:
                return n

            if n not in memo:
                memo[n] = climb(n-1) + climb(n-2) 
            return memo[n]

        return climb(n)



        