class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
        visited = defaultdict(int)

        def inbound(x,y):   #check if an index is not out of boud or not
            return x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0

        queue = deque() #r,c,level
        queue.append([0,0,1])
        visited[(0,0)] = 1

        while queue:
            node = queue.popleft()

            if not inbound(node[0],node[1]) or grid[node[0]][node[1]] ==1  and (node[0],node[1]) in visited:
                continue

            if node[0] == len(grid)-1 and  node[1] == len(grid[0])-1:
                return node[2]

            for dir in directions:
                x = node[0] + dir[0] ; y = node[1] + dir[1]
                if (x,y) not in visited:
                    queue.append([x,y,node[2]+1])
                    visited[(x,y)] = 1

        return -1



