class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=set()
        map={}

        for i in range(len(matches)):
            winner.add(matches[i][0])
            if matches[i][1] not in map:
                map[matches[i][1]]=1
            else:
                map[matches[i][1]]+=1

        print(map)
        loser=[]

        for key,values in map.items():
            if(values==1):
                loser.append(key)

        loser.sort()
        # winner.sort()
        winner=list(winner)
        winner.sort()
        total=[]
        # total.append(winner)
        # total.append(loser)
        print(total)
        print(map)
        lswinner=[]
        for i in range(len(winner)):
            if(winner[i] not in map):
                lswinner.append(winner[i])

        total.append(lswinner)
        total.append(loser)
        return total