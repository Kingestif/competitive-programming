class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        k=arr.copy()
        arr.sort()
        map={}
        rank=1
        for i in range(len(arr)):
            if arr[i] not in map:
                map[arr[i]]=rank
                rank+=1
                
        x=[]
        for i in range(len(k)):
            x.append(map[k[i]])
        return x
        
        

