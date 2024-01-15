class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # do the current then merge
        intervals.append(newInterval) ; intervals.sort()
        print(intervals)

        checked=[]
        for i in range(len(intervals)):
            if i==0:
                checked.append(intervals[i])
            elif intervals[i][0] >= checked[-1][0] and intervals[i][0] <= checked[-1][1]:
                if checked[-1][1] < intervals[i][1]:
                    checked[-1][1]=intervals[i][1]
            else:
                checked.append(intervals[i])
        return checked
        