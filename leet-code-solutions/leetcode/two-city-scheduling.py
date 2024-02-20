   
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        total=0
        map={}
        # for i in costs:
        #     map[i[0]-i[1]] = i 
        # print(map)
        # sormap = dict(sorted(map.items(),reverse=True))
        # print(sormap)
        # counter=0

        # for key,values in sormap.items():
        #     if counter < n:
        #         total += values[1]
        #         print(values[1])
        #     else:
        #         total += values[0]

        #     counter+=1
                
            

        # return total
        new = sorted(costs, key=lambda x: x[0] - x[1],reverse=True)
        counter=0
        total=0
        for i in new:
            if counter < n:
                total += i[1]
            else:
                total += i[0]
            counter+=1
        return total
