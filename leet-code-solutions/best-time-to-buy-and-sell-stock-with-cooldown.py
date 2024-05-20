class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # core: just modify the take index to skip next index after taking it, after copying another best time to seel1
        memo = defaultdict(int)
        def dp(idx,state):
            if idx >= len(prices):
                return 0

            if (idx,state) not in memo:
                if not state:   #buy
                    memo[(idx,state)] = max(dp(idx+1, not state) - prices[idx] , dp(idx+1,state))
                else:   #sell
                    memo[(idx,state)] = max(dp(idx+2, not state) + prices[idx], dp(idx+1,state))   
            return memo[(idx,state)]
            
        return dp(0,False)