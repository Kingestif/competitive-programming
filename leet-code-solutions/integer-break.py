class Solution:
    def integerBreak(self, n: int) -> int:
        memo = defaultdict(int)
        if n < 4:
            return n -1 
        def dp(k):
            if k < 4:
                return k


            if k not in memo:
                memo[k] = 0
                for i in range(1,k):
                    memo[k] = max(memo[k],i * dp(k-i))

            return memo[k]


        return dp(n)
                
