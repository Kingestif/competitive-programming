class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Core: the DFS functions is same as always 
        # first do the normal matrix DFS, then what we update is we call DFS for each matrix index and see the number of lands at that point, if we get 0 i means there is no land 

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = defaultdict(int)
        land = 0

        def inbound(x,y):   #check if an index is not out of boud or not
            if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0:
                return True
            else:
                return False


        def DFS(i,j, land):
            if grid[i][j] == "1" and (i,j) not in visited:  #counts number of lands(that surrrounds it) EACH TIME and index is called
                land += 1

            visited[(i,j)] = 1


            for dir in directions:
                x = i + dir[0]  ;   y = j + dir[1]

                if (x,y) not in visited and inbound(x,y) and grid[x][y] == "1":
                    land = DFS(x,y,land)    #bc we need the value of land to return 

            return land     

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":   #we only need to calculate DFS for grids == 1
                    land = 0    #KEY, since we want to calculate number of land each time make it 0 and pass it as argument

                    land = DFS(i,j,land)  
                    if land:    #if this is not 0 it means ther is some lands like if its 2 it means 2 lands are connected so if 0 it means there is no land connected(another way means ther is no land)
                        ans += 1
                    
        return ans
