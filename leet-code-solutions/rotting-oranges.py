class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        queue = deque()

        check = False
        checkfor1 = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    check = True

                if grid[i][j] == 1:
                    checkfor1 = True


        # visited = defaultdict(int)
        time = 0

        def inbound(x,y):   
            return x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0

        print(queue)
        while queue:
            ls = deque()
            while queue:
                val = queue.popleft()
                # visited[(val[0],val[1])] = 1
                print(val)

                isRotten = False
                # if grid[val[0]][val[1]] == 2:
                for dir in directions:
                    x = dir[0] + val[0] ;   y = dir[1] + val[1]
                    if inbound(x,y) and grid[x][y] == 1:
                        isRotten = True
                        grid[x][y] = 2  #make them rotten
                        ls.append((x,y))
                # if isRotten:
            queue = ls
            time += 1

        # if therses unrotten orange
        if not check and checkfor1:
            return -1
        elif not check and not checkfor1:
            return 0

        for row in grid:
            if 1 in row:
                return -1

        return time -1
