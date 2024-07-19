class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height,width = len(dungeon),len(dungeon[0])
        m,n = height-1,width-1
        dp = dungeon
        dp[m][n] = max(1,1-dp[m][n])

        for i in range(m-1,-1,-1):
            dp[i][n] = max(1,dp[i+1][n]-dp[i][n])

        for j in range(n-1,-1,-1):
            dp[m][j] = max(1,dp[m][j+1]-dp[m][j])

        for k in range(m-1,-1,-1):
            for l in range(n-1,-1,-1):
                dp[k][l] = max(1,min(dp[k+1][l],dp[k][l+1])-dp[k][l])

        return dp[0][0]