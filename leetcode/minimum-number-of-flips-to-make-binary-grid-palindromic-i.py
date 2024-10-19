import numpy as np
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rowflip = 0
        for i in range(len(grid)):
            x = 0 ; y = len(grid[0]) - 1
            while x < y:
                if grid[i][x] != grid[i][y]:
                    rowflip += 1
                x += 1 ; y -= 1


        colgrid = np.transpose(grid)

        colflip = 0
        for i in range(len(colgrid)):
            x = 0 ; y = len(colgrid[0]) - 1
            while x < y:
                if colgrid[i][x] != colgrid[i][y]:
                    colflip += 1
                x += 1 ; y -= 1

        return min(colflip, rowflip)

        





