class Solution:
    def numSquares(self, n: int) -> int:
        # if you store (num,perfect as the memo) itll be memory limit so only sture num
        
        perfect = 1
        memo = defaultdict(int)

        def dp(num,perfect):
            if num <= 0:
                return 0
            if perfect ** 2 > num:  #invalid 
                return float('inf')

            if num in memo:
                return memo[num]

            take = dp(num - perfect ** 2, perfect) + 1
            notake = dp(num, perfect + 1)

            memo[num] = min(take,notake)

            return memo[num]

        return dp(n,perfect)