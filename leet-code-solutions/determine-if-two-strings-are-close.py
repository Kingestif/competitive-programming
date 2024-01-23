from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False

        map=defaultdict(int)
        map2=defaultdict(int)
        for i in range(len(word1)):
            map[word1[i]]+=1
            map2[word2[i]]+=1
        print(map.values()==map2.values())
        if map.keys()!=map2.keys():
            return False

        a1=[] ; a2=[]
        for key,values in map.items():
            a1.append(values)
        for key,values in map2.items():
            a2.append(values)
        
        a1.sort() ; a2.sort()
        if a1!=a2:
            return False

        return True

        