class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        check=True
        for i in range(0,len(matrix)):
            if(check==False):
                print("nope")
                break
            for j in range(0,len(matrix[i])):
                print(matrix[i][j])
                if(i+1>=len(matrix) or j+1>=len(matrix[i])):
                    break
                if(matrix[i][j]!=matrix[i+1][j+1]):
                    check=False
            print("")

        return check
