class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        new=[]
        for i in range(len(points)):
            new.append(points[i][0])
        new.sort()

        max=float('-inf')
        for i in range(len(new)-1):
            if new[i+1] - new[i] > max:
                max=new[i+1] - new[i]
        return max


