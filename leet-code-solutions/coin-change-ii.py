class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        def dp(idx,summ):
            if idx >= len(coins):
                return 0
            if summ == 0:   #legal
                return 1
            if summ < 0:    #illegal
                return 0

            if (idx,summ) not in memo:
                take = dp(idx,summ-coins[idx]) 
                nottake = dp(idx+1,summ)
                memo[(idx,summ)] = take + nottake
            return memo[(idx,summ)]

        return dp(0,amount)




        