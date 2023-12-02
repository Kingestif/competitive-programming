class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        check=True
        flag=False
        map={}
        for i in range(len(order)):
            map[order[i]]=i
        i=0 ; j=0
        while i < len(words)-1:
            if(check==False):
                break
            j=0
            while j < len(words[i]):
                if(map[words[i][j]] == map[words[i+1][j]]):
                
                    j+=1

                    # if(j>=len(words[i])-1): #if j reaches last alphabet of words
                    #     break

                    if(j>=len(words[i+1]) and len(words[i+1])!=len(words[i])):
                        check=False
                        break
                elif(map[words[i][j]] > map[words[i+1][j]]):
                    check=False
                    break
                else:
                    break



            i+=1
        return check