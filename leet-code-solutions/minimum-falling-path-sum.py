class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = defaultdict(int)
        def inbound(x,y):  
            return x < len(matrix) and y < len(matrix[0]) and x >= 0 and y >= 0


        def dp(x,y):
            if x >= len(matrix[0]): #means we are finished
                return 0

            if not inbound(x,y):    #menas we are wrong
                return float('inf')
            
            if (x,y) not in memo:
                memo[(x,y)] = min(dp(x+1,y-1) + matrix[x][y] , dp(x+1,y) + matrix[x][y] , dp(x+1,y+1) + matrix[x][y])
            return memo[(x,y)]

        # if we just said return (0,0) itll only check the first (0,0) in the first row so we gotta iterate to all first row cells
        ans = float('inf')
        for j in range(len(matrix[0])):     #just iterate to the first row cells
            ans = min(ans,dp(0,j)) 

        return ans
