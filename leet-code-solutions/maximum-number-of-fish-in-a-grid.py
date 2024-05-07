class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = defaultdict(int)

        def inbound(x,y):   #check if an index is not out of boud or not
            if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0:
                return True
            else:
                return False

        
        def DFS(i,j,total):
            if grid[i][j] != 0 and (i,j) not in visited: 
                print(total,grid[i][j])
                total += grid[i][j]

            visited[(i,j)] = 1

            for dir in directions:
                x = i + dir[0]  ;   y = j + dir[1]

                if (x,y) not in visited and inbound(x,y) and grid[x][y] != 0:
                    total = DFS(x,y,total)    

            return total


        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    total = 0
                    total = DFS(i,j,total)
                    ans.append(total)


        if len(ans) == 0:
            return 0
        return max(ans)

        
                


