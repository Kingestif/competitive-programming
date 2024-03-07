class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        check = {}  ; ls=[] ; ans=[]
        for i in range(len(intervals)):
            check[intervals[i][0]] = i
            ls.append(intervals[i][0])
        ls.sort()
        map2={}
        sorcheck = dict(sorted(check.items()))

        index = 0
        for key,values in sorcheck.items():
            map2[index] = values
            index += 1


        for row in intervals:
            if bisect_left(ls,row[1]) >= len(ls):
                ans.append(-1)
            else:
                ans.append(map2[bisect_left(ls,row[1])])

        return ans         

