class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if(len(score)==1):
            if(score[0]==1):
                score[0]="Gold Medal"
            elif(score[0]==2):
                score[0]="Silver Medal"
            elif(score[0]==3):
                score[0]="Bronze Medal"

            return score
            
        new=score.copy()

        new = sorted(score, reverse=True)
        print(new)

        n=new.copy()
        for i in range(0,len(new)):
            if(score[i]==new[0]):
                n[i]="Gold Medal"
            elif(score[i]==new[1]):
                n[i]="Silver Medal"
            elif(score[i]==new[2]):
                n[i]="Bronze Medal"
            else:
                for x in range(0,len(new)):
                    if(score[i]==new[x]):
                        n[i]=str(x+1)


        return n