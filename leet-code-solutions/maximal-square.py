class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # approach2 bottom up dp
        def inbound(x,y):   
            return x < len(matrix) and y < len(matrix[0]) and x >= 0 and y >= 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
        
        val = 0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,-1,-1):
                if matrix[i][j] == 1:
                    if i < len(matrix) - 1 and j < len(matrix[0]) - 1:
                        matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1])
                val = max(val,matrix[i][j])
             
        return val*val
