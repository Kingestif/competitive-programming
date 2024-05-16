class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def inbound(x,y):  
            if x < m and y < n and x >= 0 and y >= 0:
                return True
            else:
                return False


        def dp(x,y):
            if not inbound(x,y):
                return 0
            if x == m-1 and y == n-1:
                return 1

            if (x,y) not in memo:
                memo[(x,y)] = dp(x+1,y) + dp(x,y+1)
            return memo[(x,y)]
            
        return dp(0,0)