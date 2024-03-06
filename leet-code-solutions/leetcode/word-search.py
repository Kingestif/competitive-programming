class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = [] ; combo = set()
        def backtrack(row,col,combo,curIdx):
            # basecase
            # curIdx is used to compare current letter from given word and that of current letter from our list 
            if curIdx == len(word):
                return True
            elif len(combo) > len(word):
                return False
            elif row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            elif (row,col) in combo:
                return False
            elif word[curIdx] != board[row][col]:    #main
                return False

            # now call the function on the 4 adjacent directions
            combo.add((row,col))
            result = (backtrack(row,col+1,combo,curIdx+1) or backtrack(row+1,col,combo,curIdx+1) or backtrack(row,col-1,combo,curIdx+1) or backtrack(row-1,col,combo,curIdx+1))
            combo.remove((row,col))
            return result



                    


        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i,j,combo,0):
                    return True
        return False