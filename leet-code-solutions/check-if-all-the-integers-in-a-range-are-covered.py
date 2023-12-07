class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s=set()
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                s.add(j)


        for i in range(left,right+1):
            if(i not in s):
                return False
        return True





