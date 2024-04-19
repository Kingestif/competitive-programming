class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = defaultdict(int)
        map = defaultdict(int)
        def inbound(x,y):   #check if an index is not out of boud or not
            return x < len(board) and y < len(board[0]) and x >= 0 and y >= 0
        
        def borderChecker(x,y):
            return (x == 0 and y == 0) or (x and y == 0) or (y and x == 0) or (x and y == len(board[0])-1) or (y and x == len(board)-1)
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                if borderChecker(i,j) and board[i][j] == "O":
                    map[(i,j)] = 1

        def DFS(i,j):
            nonlocal check
            dic.add((i,j))
            visited[(i,j)] = 1
            for dir in directions:
                x = i + dir[0] ;    y = j + dir[1]

                if (x,y) in map:
                    check = False
                if inbound(x,y) and board[x][y] == "O" and (x,y) not in visited:
                    DFS(x,y)








        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i,j) not in visited and (i,j) not in map:
                    check = True
                    dic = set()
                    DFS(i,j)
                    print(check,dic)
                    if check:
                        for iter in dic:
                            board[iter[0]][iter[1]] = "X"
                        

        



        



        


        
            
