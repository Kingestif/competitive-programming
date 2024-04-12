class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        destination = (len(grid)-1,len(grid[0])-1)  #our destination
        visited = defaultdict(int)

        map = defaultdict(int)
        map[1] = ((0,-1),(0,1))
        map[2] = ((-1,0),(1,0))
        map[3] = ((0,-1),(1,0))
        map[4] = ((0,1),(1,0))
        map[5] = ((-1,0),(0,-1))
        map[6] = ((-1,0),(0,1))

        def inbound(x,y):   
            if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0:
                return True
            else:
                return False


        def DFS(i,j):
            visited[(i,j)] = 1
            if (i,j) == destination:
                return True

            neighbour = map[grid[i][j]]

            # the 3rd CONDITION(-row[0],-row[1]): means if there is a valid path from (i, j) to (x, y), there should also be a valid path from (x, y) to (i, j), so we should check if the reverse(negative of the directions) is Also True.
            for row in neighbour:
                x = row[0] + i  ;   y = row[1] + j
                if inbound(x,y) and (x,y) not in visited and (-row[0],-row[1]) in map[grid[x][y]]:
                    val = DFS(x,y)
                    if val:
                        return True
            return False
                


        return DFS(0,0)


