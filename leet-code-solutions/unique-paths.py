class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(x,y):  
            if x < m and y < n and x >= 0 and y >= 0:
                return True
            else:
                return False


        arr = [[0]*n for i in range(m)]
        arr[m-1][n-1] = 1

        # we start from last then add 1 every time
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if inbound(i+1,j):
                    arr[i][j] += arr[i+1][j]
                if inbound(i,j+1):
                    arr[i][j] += arr[i][j+1]
                
        return arr[0][0]


        