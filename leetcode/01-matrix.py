from queue import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque()
        visited = defaultdict(int)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append([i,j,1])

        def inbound(x,y):   
            return x < len(mat) and y < len(mat[0]) and x >= 0 and y >= 0

        while queue:
            node = queue.popleft()
            for dir in directions:
                x = node[0] + dir[0] ;  y = node[1] + dir[1]
                if inbound(x,y) and mat[x][y] == 1 and (x,y) not in visited:  
                    mat[x][y] = node[2]  
                    queue.append([x,y,node[2]+1])  
                    visited[(x,y)] = 1
        return mat
                


       
                


                     

            





