from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Core:if 2 matrix index sum(i,j) is equal they are diagonal to eachother so use map to store that
        ans=[]
        map=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                map[i+j].append(mat[i][j])


        for key,values in map.items():
            if key%2==0:
                map[key].reverse()
                ans.append(map[key])
            else:
                ans.append(map[key])

        new=[]
        for row in ans:
            for col in row:
                new.append(col)

        return new


        

                