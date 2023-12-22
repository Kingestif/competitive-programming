class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        length=len(grid)
        maxi=0
        for i in range(len(grid)):
            for j in range(1,len(grid[i])-1):
                if i+2 < length :
                    total=grid[i][j] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j] + grid[i+2][j] + grid[i+2][j-1] + grid[i+2][j+1]
                    # print(grid[i][j], grid[i][j-1] ,grid[i][j+1] , grid[i+1][j] , grid[i+2][j] , grid[i+2][j-1] , grid[i+2][j+1])
                    print("heelo")
                    if total > maxi:
                        maxi=total 
                # print(maxi,i,j)
                    

        return maxi