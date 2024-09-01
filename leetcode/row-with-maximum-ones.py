class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = []
        count = 0
        maxx = 0

        for i in range(len(mat)):
            count = mat[i].count(1)
            maxx = max(maxx,count)
            ans.append((i,count))
            

        for x,y in ans:
            if y == maxx:
                return [x,y]