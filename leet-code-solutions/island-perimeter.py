class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # we use adjaceny matrix for this problem(easy)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = defaultdict(int)
        perimeter = 0
        land = 0
        diff = 0

        def inbound(x,y):   #check if an index is not out of boud or not
            if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0:
                return True
            else:
                return False


        def DFS(cell):  #cell means i,j
            nonlocal perimeter
            nonlocal diff
            nonlocal land
            visited[cell] = 1
            for dir in directions:
                i = dir[0] + cell[0]  ;   j = dir[1] + cell[1]

                if inbound(i,j) and grid[i][j] == 1 and grid[cell[0]][cell[1]]:
                    diff -= 1

            if grid[cell[0]][cell[1]] == 1:
                land += 1
            for dir in directions:
                x = dir[0] + cell[0]  ;   y = dir[1] + cell[1]

                # we check if a cell is visted, not out of bound and its grid doesnt contain water
                if (x,y) not in visited and inbound(x,y):
                    # visited[(x,y)] = 1
                    DFS((x,y))
                



        DFS((0,0))
        
        print(diff)
        print(land)
        return land * 4 + diff