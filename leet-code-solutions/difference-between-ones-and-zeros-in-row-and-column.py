class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = copy.deepcopy(grid)
        length=len(grid[0])
        

        for i in range(len(grid)):
            counter=grid[i].count(1)
            for j in range(len(grid[i])):
                diff[i][j]=counter-(length-counter)

        # print(diff)

        columns = [[row[i] for row in grid] for i in range(len(grid[0]))]
        # print(columns)

        leng2=len(columns[0])
        for i in range(len(columns)):
            counter=columns[i].count(1)
            for j in range(len(columns[i])):
                diff[j][i]+=counter-(leng2-counter)
        

    
        return diff


