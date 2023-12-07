class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        counter=0
        i=0;j=0
        # core:6 testcases you only increment if both are arr[0] and arr[1] are equal if one of them is equl incremnt or dec the other like that kind of test cases
        while i < len(points)-1:
            j=0

            while j < 2:

                if points[i][j]==points[i+1][j] and points[i][j+1]==points[i+1][j+1] :
                    break

                elif points[i][j]==points[i+1][j] or points[i][j+1]==points[i+1][j+1]:
                
                    if points[i][j+1]==points[i+1][j+1]:
                        if points[i][j]>points[i+1][j]:
                            points[i][j]-=1
                            counter+=1
                        else:
                            points[i][j]+=1
                            counter+=1

                    elif points[i][j]==points[i+1][j]:
                        if points[i][j+1]>points[i+1][j+1]:
                            points[i][j+1]-=1
                            counter+=1
                        else:
                            points[i][j+1]+=1
                            counter+=1

                elif(points[i][j]>points[i+1][j] and points[i][j+1]>points[i+1][j+1]):
                    points[i][j]-=1
                    points[i][j+1]-=1
                    counter+=1

                elif(points[i][j]<points[i+1][j] and points[i][j+1]<points[i+1][j+1]):
                    points[i][j]+=1
                    points[i][j+1]+=1
                    counter+=1

                elif(points[i][j]<points[i+1][j] and points[i][j+1]>points[i+1][j+1]):
                    points[i][j]+=1
                    points[i][j+1]-=1
                    counter+=1

                elif(points[i][j]>points[i+1][j] and points[i][j+1]<points[i+1][j+1]):
                    points[i][j]-=1
                    points[i][j+1]+=1
                    counter+=1

            i+=1






        return counter





