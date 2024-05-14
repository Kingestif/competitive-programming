class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # refer FunkyLlama problem first(A, limited choices)
        memo = defaultdict(int)
    
        def dp(summ):
            if summ == amount:
                return 0
            if summ > amount:
                return float('inf')


            if summ not in memo:
                memo[summ] = float('inf')  #when we say dp(0) itll be set to float('-inf') so that the max will not be affected, itll get updated inside loop
                for i in range(0,len(coins)):
                    memo[summ] = min((1 + dp(summ + coins[i]),memo[summ]))
            return memo[summ]

        ans = dp(0)
        if ans == float('inf'): 
            return -1
        return ans