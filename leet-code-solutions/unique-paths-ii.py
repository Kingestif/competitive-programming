class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. top to bottom approach
        memo = defaultdict(int)
        def inbound(x,y):  
            return x < len(obstacleGrid) and y < len(obstacleGrid[0]) and x >= 0 and y >= 0
        
        def dp(i,j):
            if not inbound(i,j) or obstacleGrid[i][j] == 1:    #not allowed
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1

            if (i,j) not in memo:
                memo[(i,j)] = dp(i+1,j) + dp(i,j+1)
            return memo[(i,j)]

        return dp(0,0)