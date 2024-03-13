from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check if the dictionaries are the same O(26) so O(n)
        def isvalid(map1,map2): 
            for key,values in map2.items():
                if map1[key] < values:
                    return False
            return True

        start = 0 ; end = 0
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        maxi = float('inf')

        for i in range(len(t)):
            map2[t[i]] += 1
    
        minim = [0,len(s)]
        while start <= end :
            if isvalid(map1,map2):
                maxi = min(maxi,end - start)
                if end - start < minim[1] - minim[0]:
                    minim = [start,end]
                map1[s[start]] -= 1
                start += 1
            else:
                if end >= len(s):
                    break
                map1[s[end]] += 1
                end += 1
        if maxi == float('inf'):
            return ""
        return s[minim[0] : minim[1]]
            





        