class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = defaultdict(int)

        def dp(start,end):
            if start > end:
                return 0
            
            if (start,end) not in memo:
                memo[(start,end)] = max(dp(start+1,end) + piles[start], dp(start,end-1) + piles[end])   
            return memo[(start,end)]


        val = dp(0,len(piles)-1)

        if val > sum(piles) // 2:   #means nomatter what Bob choose since the max half is chosen by alice it cant win!
            return True
        return False