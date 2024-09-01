class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        newgrid = list(map(list,zip(*grid)))
        ls = []
        for row in newgrid:
            maxx = max(row)
            minn = min(row)
            ls.append(max(len(str(maxx)), len(str(minn))))
            

        return ls


