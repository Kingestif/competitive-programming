import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map={}
        iterator=0
        for row in points:
            value=pow(row[0],2)+pow(row[1],2)
            if (row[0],row[1]) not in map:
                map[row[0],row[1]]=value
            else:
                map[row[0],row[1],iterator]=value
            iterator+=1



        ans=[]

        sorted_dict = dict(sorted(map.items(), key=lambda x: x[1]))

        print(sorted_dict)

        for key,values in sorted_dict.items():
            print(key)
            if k==0:
                break
            else:
                k-=1
                ans.append([key[0],key[1]])
        return ans
            
        