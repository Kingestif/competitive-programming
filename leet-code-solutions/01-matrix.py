from queue import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # use BFS
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque()
        visited = defaultdict(int)

        # since all 0's are found on level 1 first append them to our queue
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append([i,j,1])

        def inbound(x,y):   
            return x < len(mat) and y < len(mat[0]) and x >= 0 and y >= 0

        # Core: whenever we reach a grid with 1 we assign the current level to it and increment level of our current level(1's level) by 1
        while queue:
            node = queue.popleft()
            for dir in directions:
                x = node[0] + dir[0] ;  y = node[1] + dir[1]
                if inbound(x,y) and mat[x][y] == 1 and (x,y) not in visited:  #the shortest path to this cell is from the node we have now!!
                    mat[x][y] = node[2]  #like we said, whenever we reach 1 we assign it our caller coordinate
                    queue.append([x,y,node[2]+1])   #then we increment b/c this is our next depth
                    visited[(x,y)] = 1
        return mat
                


       
                


                     

            





