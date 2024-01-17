class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map={}
        for i in range(0,len(arr)):
            if(arr[i] not in map):
                map[arr[i]]=1
            else:
                map[arr[i]]+=1

        check=True
        print(map)
        # print(4 in map.values())
        for key in map:
            temp=map[key]
            map[key]=float('inf')
            if(temp in map.values()):
                check=False
            print(key)

        return check