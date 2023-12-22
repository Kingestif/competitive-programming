import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # contraint1
        for row in board:
            map={}
            for col in row:
                if col.isdigit():
                    if col not in map:
                        map[col]=0
                    else:
                        print("const1")
                        return False

        # constraint2
        for i in range(9):
            map2={}
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] not in map2:
                        map2[board[j][i]]=0
                    else:
                        print("const2")
                        return False

        # constraint3
        board=np.array(board)
        i=0
        while i<=6:
            j=0
            end=i+3
            while j<=6:
                end2=j+3
                slice1=board[i:end,j:end2]
                # print(slice1)
                map3={}
                for row in slice1:
                    for col in row:
                        if col.isdigit():
                            if col not in map3:
                                map3[col]=0
                            else:
                                print("const3",slice1)
                                return False
                j+=3

            i+=3
        return True



            
        



