class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map={}
        check=[]

        for i in range(len(paths)):
            map[paths[i][0]]=1

            if paths[i][1] not in map:
                map[paths[i][1]]=0
                check.append(paths[i][1])
            else:
                map[paths[i][1]]=1

        for key,value in map.items():
            if value==0:
                return key





                

            
