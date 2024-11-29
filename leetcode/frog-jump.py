class Solution:
    def canCross(self, stones: List[int]) -> bool:
        check = defaultdict(int)
        for i in stones:
            check[i] = 1

        last = stones[-1]
        memo = defaultdict(int)
        def dp(position,jump):
            nonlocal last
            if position == last:
                return True
            if position not in check or jump <= 0:
                return False

            if (position,jump) not in memo:
                memo[(position,jump)] = dp(position + jump - 1,jump-1) or dp(position+jump,jump) or dp(position+ jump+1,jump+1)
            return memo[(position,jump)]

        return dp(1,1)
        