class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        map={}
        min=float('inf')
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                map[fronts[i]]=i
        check=False
        for i in range(len(fronts)):
            if fronts[i] not in map and fronts[i]<min:
                min=fronts[i]
                check=True
            if backs[i] not in map and backs[i]<min:
                min=backs[i]
                check=True
            

        if check==True:
            return min
        else:
            return 0






