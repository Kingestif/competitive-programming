class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        length=len(matrix)
        self.matrix = matrix
        self.prefix=[0]*(len(matrix[0]) + 1)
        self.prematrix = []

        #create the 0 by 0 empty matrix
        for i in range(len(matrix) + 1):
            self.prematrix.append(self.prefix[:])  #the ":" part creates new referecne for each row if not there , modification to one row apply to all other
        
        #works out prefix sum of each row, and just add full 0s row and 0s column for calculation
        for row in range(len(self.matrix)):
            presum=0
            for col in range(len(self.matrix[row])):
                presum += self.matrix[row][col]
                self.prematrix[row+1][col+1] = presum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1 ; col1+=1 ; row2+=1 ; col2+=1
        summ=0
        for i in range(row1,row2+1):
            summ += (self.prematrix[i][col2] - self.prematrix[i][col1 - 1])
        return summ





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)