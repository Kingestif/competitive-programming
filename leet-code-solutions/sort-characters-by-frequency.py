from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        map=defaultdict(int) ; newmap={}    ; arr=[]
        for i in s:
            map[i]+=1
        
        for key,values in map.items():
            newmap[values,key]=key

        for key, values in sorted(newmap.items(),reverse=True):
            arr.append(key[0] * values)

        arr="".join(arr)
        return arr
