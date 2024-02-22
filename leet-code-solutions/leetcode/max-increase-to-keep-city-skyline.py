from collections import defaultdict
from collections import Counter
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        hormap=defaultdict(int)   
        varmap=defaultdict(int)
        total = 0

        # for horizontal maximums
        for i in range(len(grid)):
            max=float('-inf')
            for j in range(len(grid[i])):
                if grid[i][j] > max:
                    max = grid[i][j]
                    a=i ; b=j
            hormap[i] = grid[a][b]
        # print(hormap)

        # for vertical maximums
        for i in range(len(grid[0])):
            max=float('-inf')
            for j in range(len(grid)):
                if grid[j][i] > max:
                    max=grid[j][i]
                    a=i
                    b=j
            varmap[i]=grid[b][a]
        # print(varmap)

        # for comparison
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num = min(varmap[j],hormap[i])
                total += num - grid[i][j] 


        return total
            