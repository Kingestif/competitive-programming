class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        counter=1
        points = sorted(points, key=lambda x: x[1])
        num=points[0][1]

        print(points)
        for i in points:
            if num < i[0] or num > i[1]:
                counter += 1
                num = i[1]
        return counter

                

        return 0
        