class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        # modification: add "trnas" variable that keeps count of transactions, it gets incremented whenever you sell a stock(so only sells after buying)
        def dp(idx,state,trans):
            if idx >= len(prices):
                return 0
            if trans >= 2:
                return 0

            if (idx,state,trans) not in memo:
                if not state:   #buy
                    memo[(idx,state,trans)] = max(dp(idx+1, not state,trans) - prices[idx] , dp(idx+1,state,trans))
                else:   #sell
                    memo[(idx,state,trans)] = max(dp(idx+1, not state,trans+1) + prices[idx], dp(idx+1,state,trans))   
            return memo[(idx,state,trans)]
            
        return dp(0,False,0)