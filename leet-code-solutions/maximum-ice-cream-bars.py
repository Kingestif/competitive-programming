class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxx=max(costs) + 1
        temp=[0]*maxx

        # occurece
        for i in range(len(costs)):
            temp[costs[i]]+=1

        temp2=[0]*maxx
        total=0
        # accumulative
        for i in range(len(temp)):
            temp2[i]=total
            total+=temp[i]


        temp3=[0]*len(costs)
        # add then inc
        for i in range(len(costs)):
            temp3[temp2[costs[i]]]=costs[i]
            temp2[costs[i]]+=1


        ans=0
        for i in temp3:
            if coins - i >=0:
                coins-=i
                ans+=1

        return ans








