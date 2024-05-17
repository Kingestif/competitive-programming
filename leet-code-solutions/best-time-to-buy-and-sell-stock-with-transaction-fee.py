class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        def dp(idx,state):
            if idx >= len(prices):
                return 0

            if (idx,state) not in memo:
                if not state:   #we are buying,  take $ not take
                    memo[(idx,state)] = max(dp(idx+1, not state) - prices[idx] , dp(idx+1,state))
                else:
                    memo[(idx,state)] = max(dp(idx+1, not state) + prices[idx] - fee, dp(idx+1,state))   #sell it or call the next one
            return memo[(idx,state)]
            

            



        return dp(0,False)