from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter=[]
        map=defaultdict(int)
        for i in p:
            map[i]+=1
        
        checker=defaultdict(int)

        for i in range(len(s)):
            if i < len(p):
                checker[s[i]]+=1
            else:
                if checker==map:
                    counter.append(i-len(p))

                checker[s[i-len(p)]]-=1
                if checker[s[i-len(p)]]==0:
                    del checker[s[i-len(p)]]
                checker[s[i]]+=1

            if i==len(s)-1:
                if checker==map:
                    counter.append(i-len(p)+1)



        print(checker)
        return counter
                    



        







        