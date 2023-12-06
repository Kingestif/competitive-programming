class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map={}
        min=float('inf')
        smin=""
        for i in range(len(list1)):
            if(list1[i] not in map):
                map[list1[i]]=i
        for j in range(len(list2)):
            if(list2[j] in map):
                if(map[list2[j]] + j < min):
                    min=map[list2[j]]+j
                    smin=list2[j]
                elif map[list2[j]] + j == min:
                    smin+=","
                    smin+=list2[j]


        smin="".join(smin)
        smin=smin.split(',')
        return smin




        