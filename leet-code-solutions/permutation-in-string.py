from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map=defaultdict(int)
        map2=defaultdict(int)
        start=0 ; end=0

        for i in range(len(s1)):
            map[s1[i]]+=1

        # for i in range(len(s2)):
        #     if s2[i] not in s1:
        #         map2={}
        #     else:
        #         map2[s2[i]]+=1
        #         if map2[s2[i]]>map[s2[i]]:
        #             map2={}
            
        # return True
        while end<len(s2):
            if s2[end] in s1:
                if map2[s2[end]] < map[s2[end]]:
                    map2[s2[end]]+=1
                    end+=1
                    if sum(map2.values())==sum(map.values()):
                        return True
                else:
                    map2[s2[start]]-=1
                    start+=1
            else:
                map2.clear()
                end+=1
                start=end
        return False
